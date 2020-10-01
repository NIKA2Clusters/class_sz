#! python3
#e.g., python3 sz_auxiliary_files/run_scripts/tSZ_varying_params.py -param_name sigma8 -min 0.7 -max 0.9 -N 5 -spacing log -show_legend yes -show_error_bars yes -output ' ' -save_tsz_ps no -save_figure no -plot_redshift_dependent_functions yes
# $ python3 sz_auxiliary_files/run_scripts/tSZ_varying_params.py -param_name sigma8 -min 0.8 -max 0.9 -N 1 -spacing log -show_legend yes -show_error_bars no -output 'tSZ_lens_1h' -plot_tSZ_lens yes -plot_isw_lens no  -plot_isw_tsz no -plot_isw_auto no -save_tsz_ps no -save_figure no -plot_redshift_dependent_functions no
# $ $ python3 sz_auxiliary_files/run_scripts/tSZ_varying_params.py -param_name 'Frequency for y-distortion in GHz' -p_val '[100.,143.,353.]'  -show_legend yes -show_error_bars no -output 'tSZ_lens_1h' -plot_tSZ_lens yes -plot_isw_lens no  -plot_isw_tsz no -plot_isw_auto no -save_tsz_ps no -save_figure no -plot_redshift_dependent_functions no
# $ python3 sz_auxiliary_files/run_scripts/tSZ_varying_params.py -param_name 'h' -p_val '[0.7]'  -show_legend yes -show_error_bars no -output 'tSZ_gal_1h' -plot_tSZ_gal yes -plot_tSZ_lens no -plot_isw_lens no  -plot_isw_tsz no -plot_isw_auto no -save_tsz_ps no -save_figure yes -plot_redshift_dependent_functions no -y_min 1e-15 -y_max 1e-10
# isw-phi :
# $ python3 sz_auxiliary_files/run_scripts/tSZ_varying_params.py -param_name 'h' -p_val '[0.5,0.6,0.7,0.8]'  -show_legend yes -show_error_bars no -output 'isw_lens,tCl,lCl' -plot_tSZ_lens no -plot_isw_lens yes  -plot_isw_tsz no -plot_isw_auto no -save_tsz_ps no -save_figure yes -plot_redshift_dependent_functions no -y_min 1e-18 -y_max 1e-9
# yxg : careful with zmax, still some bug to figure out after z2SZ>4 blue returns inf
# $ python3 sz_auxiliary_files/run_scripts/tSZ_varying_params.py -param_name 'unwise_galaxy_sample_id' -p_val '["red","green","gr_shallow","blue"]'  -show_legend yes -show_error_bars no -output 'tSZ_gal_1h' -plot_tSZ_gal yes -plot_tSZ_lens no -plot_isw_lens no  -plot_isw_tsz no -plot_isw_auto no -save_tsz_ps no -save_figure yes -plot_redshift_dependent_functions no


# CMD for comparison:
# $ python3 sz_auxiliary_files/run_scripts/compute_and_plot_yxg_comparison_with_KA20.py -param_name 'h' -p_val '[0.6766]'  -show_legend yes -show_error_bars no -output 'tSZ_gal_1h' -plot_tSZ_gal yes -plot_tSZ_lens no -plot_isw_lens no  -plot_isw_tsz no -plot_isw_auto no -save_tsz_ps no -save_figure yes -plot_redshift_dependent_functions no
# gxg 1-halo and 2-halo
# $ python3 sz_auxiliary_files/run_scripts/compute_and_plot_yxg_comparison_with_KA20.py -param_name 'h' -p_val '[0.6766]'  -show_legend yes -show_error_bars no -output 'gal_gal_2h,gal_gal_1h' -plot_gal_gal yes -plot_tSZ_gal no -plot_tSZ_lens no -plot_isw_lens no  -plot_isw_tsz no -plot_isw_auto no -save_tsz_ps no -save_figure yes -plot_redshift_dependent_functions no

import argparse
import numpy as np
import os
import subprocess
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from scipy import interpolate
from scipy import stats
from datetime import datetime
import ast
import itertools


hplanck=6.62607004e-34 #m2 kg / s
kb = 1.38064852e-23 #m2 kg s-2 K-1
Tcmb =  2.725 #K

def g_nu(nu_in_GHz):
    nu_in_Hz = nu_in_GHz*1e9
    x = (hplanck*nu_in_Hz/kb/Tcmb)
    return (x/np.tanh(x/2.)-4.)




path_to_class = '/Users/boris/Work/CLASS-SZ/SO-SZ/class_sz/'
FIG_DIR = '/Users/boris/Work/CLASS-SZ/SO-SZ/class_sz/sz_auxiliary_files/run_scripts/figures'


def scientific_notation(p_value,digit=2):
    str_xinj_asked = str("%.3e"%p_value)
    text_gamma_str1 = ''
    if p_value>1.:
        num = float(str_xinj_asked.split('e+')[0])
        exp = int(str_xinj_asked.split('e+')[1])
        if (round(num,digit)==10.):
            num = 1.
            exp = exp + 1
        if digit == 1:
            text_gamma_str1 = r'$%.1f \times 10^{%d}$'% (num,exp)
        if digit == 2:
            text_gamma_str1 = r'$%.2f \times 10^{%d}$'% (num,exp)
        if digit == 0:
            text_gamma_str1 = r'$%.0f \times 10^{%d}$'% (num,exp)
        if num == 1.:
            text_gamma_str1 = r'$10^{%d}$'% (exp)
    if p_value<1.:
        num = float(str_xinj_asked.split('e-')[0])
        exp = int(str_xinj_asked.split('e-')[1])
        if (round(num,digit)==10.):
            num = 1.
            exp = exp - 1
        if digit == 1:
            text_gamma_str1 = r'$%.1f \times 10^{-%d}$'% (num,exp)
        if digit == 2:
            text_gamma_str1 = r'$%.2f \times 10^{-%d}$'% (num,exp)
        if digit == 0:
            text_gamma_str1 = r'$%.0f \times 10^{-%d}$'% (num,exp)
        if num == 1.:
            text_gamma_str1 = r'$10^{-%d}$'% (exp)
    if p_value==1.:
        text_gamma_str1 = r'$1$'
    return text_gamma_str1



r_dict = {} #dictionary of results
def run(args):
    # if(args.plot_ref_data == 'yes'):
    #     parameter_file = 'class-sz_chill_B12_parameters.ini'
    # else:
    #     parameter_file = 'class-sz_parameters.ini'
    parameter_file = 'class-sz_parameters_KA20.ini'
    #'class-sz_chill_B12_parameters.ini'
    #parameter_file = 'class-sz_parameters_rotti++20.ini'
    #parameter_file ='tSZ_params_ref_resolved-rotti++20_snr12_step_2.ini'
    # parameter_file = 'class-sz_chill_B12_parameters.ini'
    #parameter_file = 'class-sz_parameters_for_sz_ps_completeness_analysis_rotti++20.ini'


    os.chdir(path_to_class)
    #collect arguments
    param_name = args.param_name
    print(param_name)

    if (param_name == 'sigma8'):
        label_key = r'$\sigma_8$'
    elif (param_name == 'B'):
        label_key = r'$B$'
    elif (param_name == 'h'):
        label_key = r'$h$'
    elif (param_name == 'Omega_cdm'):
        label_key = r'$\Omega_\mathrm{m}$'
    elif (param_name == 'M2SZ'):
        label_key = r'$M_\mathrm{max}$'
    elif (param_name == 'z2SZ'):
        label_key = r'$z_\mathrm{max}$'
    elif (param_name == 'M1SZ'):
        label_key = r'$M_\mathrm{min}$'
    elif (param_name == 'm_ncdm'):
        label_key = r'$\Sigma m_\mathrm{\nu}$'
    elif (param_name == 'signal-to-noise cut-off for ps completeness analysis'):
        label_key = r'$q_\mathrm{cut}$'
    else:
        label_key = 'val'


    if args.p_val:
        p = np.asarray(ast.literal_eval(args.p_val))
        args.N = len(p)
        N = args.N
    else:
        p_min = float(args.p_min)
        p_max = float(args.p_max)
        N = int(args.N)
        spacing = args.spacing
        #define array of parameter values
        if(spacing=='log'):
            p = np.logspace(np.log10(p_min),np.log10(p_max),N)
        elif(spacing=='lin'):
            p = np.linspace(p_min,p_max,N)


    # p_min = float(args.p_min)
    # p_max = float(args.p_max)
    # N = int(args.N)
    # spacing = args.spacing


    #array to store results
    cl_1h = []
    trispectrum = []
    multipoles = []
    col = []
    val_label = []
    y_err = []
    cl_2h = []
    te_y_y = []
    kSZ_kSZ_gal_1halo = []
    tSZ_tSZ_tSZ_1h = []
    tSZ_gal_1h = []
    gal_gal_1h = []
    gal_gal_2h = []
    tSZ_lens_1h = []
    tSZ_lens_2h = []
    isw_lens = []
    isw_tsz = []
    isw_auto = []


    redshift_dependent_functions_z = []
    redshift_dependent_functions_Q = []
    #
    # #define array of parameter values
    # if(spacing=='log'):
    #     p = np.logspace(np.log10(p_min),np.log10(p_max),N)
    # elif(spacing=='lin'):
    #     p = np.linspace(p_min,p_max,N)

    #load template parameter file into dictionnary
    p_dict = {}
    with open(path_to_class+"sz_auxiliary_files/run_scripts/" + parameter_file) as f:
        for line in f:
            x = line.strip()
            if not x.startswith("#"):
                print(x.split('='))
                (key, val) = x.split('=')
                (key, val) = (key.strip(), val.strip())
                p_dict[key] = val
    #print(p_dict)
    #p_dict['h'] = 0.65
    #set correct Output
    # p_dict['output'] = 'tSZ_1h'
    p_dict['mass function'] = 'T10'  #fiducial  T10
    p_dict['pressure profile'] = 'P13' #fiducial B12
    p_dict['galaxy_sample'] = "WIxSC"
    p_dict['use_simplified_hod'] = "no"

    # masses are in M_sun, not M_sun/h
    # 'b_hydro': 0.4656
    p_dict['B'] = 1./(1.-0.4656)
    # 'Omega_c': 0.26066676
    p_dict['Omega_cdm'] = 0.26066676
    # 'Omega_b': 0.048974682
    p_dict['Omega_b'] = 0.048974682
    # 'h': 0.6766
    p_dict['h'] = 0.6766
    # 'sigma8': 0.8102
    p_dict['sigma8'] = 0.8102
    # 'n_s': 0.9665
    p_dict['n_s'] = 0.9665
    # 'lMmin': 11.99
    p_dict['M_min_HOD'] = pow(10.,11.99)*p_dict['h'] # convert to Msun/h
    # 'lM0': 11.99
    # 'lM1': 13.23
    p_dict['M1_prime_HOD'] = pow(10.,13.23)*p_dict['h'] # convert to Msun/h
    # 'sigmaLogM': 0.15
    p_dict['sigma_lnM_HOD'] = 0.15
    # 'r_corr_gy': -0.5492
    p_dict['r_corr_gy'] = -0.5492
    # 'mass_function': <class 'pyccl.halos.hmfunc.MassFuncTinker08'>
    # 'halo_bias': <class 'pyccl.halos.hbias.HaloBiasTinker10'>

    p_dict['use_central_hod'] = "yes" # ug_at_ell  = (1./ng_bar)*(nc+ns*us);
    p_dict['non linear'] = 'halofit'

    # DA: In the previous pipeline (that generated the plots in Nick's paper)
    # we were removing stuff at the edges of the redshift interval
    # to make all the integral faster (basically the integrals in z
    # were in the range of redshifts where the N(z) was at least 0.5% of its maximum value).
    # For the particular redshift bin I sent this cut removes z < 0.0175 and z > 0.4365.
    # We checked that the results are stable to this cut, which they are,
    # since the 1-halo term is completely subdominant at these low ells.
    p_dict['z1SZ']  = 0.0175
    p_dict['z2SZ']  = 0.4365




    # p_dict['create_ref_trispectrum_for_cobaya'] = 'NO'
    # p_dict['background_verbose'] = 2
    # p_dict['thermodynamics_verbose'] = 2
    p_dict['sz_verbose'] = 2
    p_dict['root'] = 'sz_auxiliary_files/run_scripts/tmp/class-sz_tmp_'
    p_dict['write sz results to files'] = 'yes' # this writes  PS and f(z)
    p_dict['pressure_profile_epsabs'] = 1.e-8
    p_dict['pressure_profile_epsrel'] = 1.e-3
    p_dict['redshift_epsabs'] = 1.e-40
    p_dict['redshift_epsrel'] = 1.e-10 # fiducial value 1e-8
    p_dict['mass_epsabs'] = 1.e-40
    p_dict['mass_epsrel'] = 1e-10

    p_dict['dlogell'] = 0.2
    #p_dict['units for tSZ spectrum'] = 'muK2'
    #p_dict['redshift_epsabs'] = 1.e-17
    #p_dict['mass_epsabs'] = 1.e-15
    #p_dict['redshift_epsrel'] = 1.e-9
    #p_dict['mass_epsrel'] = 1.e-9
    p_dict['ndimSZ'] = 100
    p_dict['n_arraySZ'] = 100
    p_dict['Frequency for y-distortion in GHz'] = 143.
    p_dict['component of tSZ power spectrum'] = 'total'
    p_dict['temperature contributions'] = 'lisw'
    p_dict['early/late isw redshift'] = p_dict['z2SZ']
    #p_dict['tol_shooting_1d'] = 1e-2
    if(args.output):
        print(args.output)
        p_dict['output'] = args.output
    # if (args.plot_redshift_dependent_functions == 'yes'):
    #     p_dict['output'] = args.output


    # if(args.plot_ref_data == 'yes'):
    #     #L = np.loadtxt('/Users/boris/Work/CLASS-SZ/SO-SZ/class_sz/sz_auxiliary_files/chill_cltsz_data.txt')
    L_ref = np.loadtxt('/Users/boris/Work/CLASS-SZ/SO-SZ/class_sz/sz_auxiliary_files/WIxSC_galaxy_ditributions/cl4boris.txt')
    ell_KA20 = L_ref[:,0]
    cl_gg_1h_KA20 = L_ref[:,1]
    cl_gg_2h_KA20 = L_ref[:,2]
    cl_yg_1h_KA20 = L_ref[:,3]
    #     L_ref = np.loadtxt('/Users/boris/Work/CLASS-SZ/SO-SZ/class_sz/output/class-sz_tmp_szpowerspectrum_mnu_0d02_ref.txt')
    #     multipoles_ref = L_ref[:,0]
    #     cl_1h_ref = L_ref[:,1]


    #prepare the figure
    label_size = 12
    title_size = 15
    legend_size = 13
    handle_length = 1.5
    if (args.print_rel_diff == 'yes'):
        fig, (ax1,ax2) = plt.subplots(2,1,figsize=(7,7))
    else:
        fig, ax1 = plt.subplots(1,1,figsize=(7,5))
    ax = ax1
    ax.tick_params(axis = 'x',which='both',length=5,direction='in', pad=10)
    ax.tick_params(axis = 'y',which='both',length=5,direction='in', pad=5)
    ax.xaxis.set_ticks_position('both')
    ax.yaxis.set_ticks_position('both')
    plt.setp(ax.get_yticklabels(), rotation='horizontal', fontsize=label_size)
    plt.setp(ax.get_xticklabels(), fontsize=label_size)
    ax.grid( b=True, which="both", alpha=0.3, linestyle='--')



    if (args.plot_redshift_dependent_functions == 'yes'):
        ax.set_xlabel(r'$z$',size=title_size)
        #ax.set_ylabel(r'$Q(z)$',size=title_size)
        ax.set_ylabel(r'$\bar{n}_g=\int_{M_{min}}^{M_{max}}dM dn/dM$',size=title_size)
        #ax.set_ylabel(r'$v_\mathrm{rms}\quad [\mathrm{km/s}]$',size=title_size)
        ax.set_xscale('linear')
        ax.set_yscale('log')
        # ax.set_xlim(0.,6.)
        # ax.set_ylim(0.,600.)
    else:
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.set_xlabel(r'$\ell$',size=title_size)
        if (args.plot_trispectrum == 'yes'):
            ax.set_ylabel(r'$T_{\ell,\ell}$',size=title_size)
        elif (args.plot_te_y_y == 'yes'):
            ax.set_ylabel(r'$\mathrm{T_e^{tSZ}} \quad [\mathrm{keV}]$',size=title_size)
        elif (args.plot_kSZ_kSZ_gal_1halo == 'yes'):
            ax.set_ylabel(r'$\mathrm{b^{kSZ^2-g}_{\ell_1,\ell_2,\ell_3}}$',size=title_size)
        elif (args.plot_tSZ_tSZ_tSZ_1h == 'yes'):
            ax.set_ylabel(r'$\mathrm{b^{y-y-y}_{\ell_1,\ell_2,\ell_3}}$',size=title_size)
        elif (args.plot_tSZ_gal == 'yes'):
            ax.set_ylabel(r'$\mathrm{C^{yg}_\ell}$',size=title_size)
        elif (args.plot_gal_gal == 'yes'):
            ax.set_ylabel(r'$\mathrm{C^{gg}_\ell}$',size=title_size)
        elif (args.plot_tSZ_lens == 'yes'):
            ax.set_ylabel(r'$\ell^2(\ell+1)\mathrm{C^{y\phi}_\ell/2\pi}$ [$\mu$K]',size=title_size)
        elif (args.plot_isw_lens == 'yes'):
            ax.set_ylabel(r'$\ell(\ell+1)\mathrm{C^{ISW\times\phi}_\ell/2\pi}$',size=title_size)
        elif (args.plot_isw_tsz == 'yes'):
            ax.set_ylabel(r'$\ell(\ell+1)\mathrm{C^{ISW\times y}_\ell/2\pi}$',size=title_size)
        elif (args.plot_isw_auto == 'yes'):
            ax.set_ylabel(r'$\ell(\ell+1)\mathrm{C^{ISW\times ISW}_\ell/2\pi}$',size=title_size)
        else:
            ax.set_ylabel(r'$10^{12}\ell(\ell+1)\mathrm{C^{yy}_\ell/2\pi}$',size=title_size)


    if(args.y_min):
        ax.set_ylim(bottom=float(args.y_min))
    if(args.y_max):
        ax.set_ylim(top=float(args.y_max))
    if(args.f_sky):
        f_sky = float(args.f_sky)
    else:
        f_sky = 1.

    colors = iter(cm.viridis(np.linspace(0, 1, N)))



    if (args.compute_scaling_with_param == 'yes'):
        #declare list to store cl at l=100
        cl_1h_100 = []
    if(int(args.N)>0):
        #loop over parameter values
        id_p = 0
        for p_val in p:
            #update dictionnary with current value
            p_dict[param_name] = p_val
            subprocess.call(['rm','-r','-f',path_to_class+'sz_auxiliary_files/run_scripts/tmp'])
            subprocess.call(['mkdir','-p',path_to_class+'sz_auxiliary_files/run_scripts/tmp'])
            with open(path_to_class+'sz_auxiliary_files/run_scripts/tmp/tmp.ini', 'w') as f:
                for k, v in p_dict.items():
                    f.write(str(k) + ' = '+ str(v) + '\n')
            startTime = datetime.now()
            subprocess.call(['./class',path_to_class+'sz_auxiliary_files/run_scripts/tmp/tmp.ini'])
            print("time in class -> " + str((datetime.now() - startTime)))
            #print(datetime.now() - startTime)


            if (param_name == 'Omega_cdm'):
                p_val = p_val + float(p_dict['Omega_b'])
            elif (param_name == 'm_ncdm'):
                p_val = 3.*p_val
            #val_label.append(label_key + ' = %.2e'%(p_val))
            if (param_name == 'm_ncdm'):
                val_label.append(label_key + ' = %3.0f'%(1000*p_val)+ ' meV')
            if (param_name == 'use_central_hod'):
                val_label.append(label_key + ' = %d'%(p_val))
            if (param_name == 'unwise_galaxy_sample_id'):
                val_label.append('%s'%(p_val))
            else:
                val_label.append(label_key + ' = ' + scientific_notation(p_val))
                #val_label.append(label_key + ' = ' + "%.2f"%(p_val))

            col.append(next(colors))


            if (args.plot_redshift_dependent_functions == 'yes'):
                R = np.loadtxt(path_to_class+'sz_auxiliary_files/run_scripts/tmp/class-sz_tmp_redshift_dependent_functions.txt')
                redshift_dependent_functions_z.append(R[:,0])
                redshift_dependent_functions_Q.append(R[:,9]) # 6: v2rms, 7: sigma2_hsv, 8: m200m/m200c @ m200m = 10^{13.5} Msun/h
                if (val_label[id_p] == 'gr_shallow'):
                    ax.plot(redshift_dependent_functions_z[id_p],redshift_dependent_functions_Q[id_p],color='forestgreen',ls='--',alpha = 1.,label = val_label[id_p])
                elif (val_label[id_p] == 'green'):
                    ax.plot(redshift_dependent_functions_z[id_p],redshift_dependent_functions_Q[id_p],color='green',ls='-',alpha = 1.,label = val_label[id_p])
                elif (val_label[id_p] == 'blue'):
                    ax.plot(redshift_dependent_functions_z[id_p],redshift_dependent_functions_Q[id_p],color='blue',ls='-',alpha = 1.,label = val_label[id_p])
                elif (val_label[id_p] == 'red'):
                    ax.plot(redshift_dependent_functions_z[id_p],redshift_dependent_functions_Q[id_p],color='red',ls='-',alpha = 1.,label = val_label[id_p])
                else:
                    ax.plot(redshift_dependent_functions_z[id_p],redshift_dependent_functions_Q[id_p],color=col[id_p],ls='-',alpha = 1.,label = val_label[id_p])



            elif ('tSZ_1h' in p_dict['output'] or 'kSZ_kSZ_gal_1h' in p_dict['output'] \
            or 'tSZ_lens_1h' in p_dict['output'] or 'tSZ_lens_2h' in p_dict['output'] \
            or 'tSZ_gal' in p_dict['output'] or 'isw_lens' in p_dict['output'] \
            or 'gal_gal' in p_dict['output']\
            or 'isw_tsz' in p_dict['output']  or 'isw_auto' in p_dict['output']):
                R = np.loadtxt(path_to_class+'sz_auxiliary_files/run_scripts/tmp/class-sz_tmp_szpowerspectrum.txt')
                multipoles.append(R[:,0])
                cl_1h.append(R[:,1])
                y_err.append(R[:,5]/np.sqrt(f_sky))
                cl_2h.append(R[:,6])
                #print(cl_2h)
                trispectrum.append(R[:,3])
                te_y_y.append(R[:,7])
                kSZ_kSZ_gal_1halo.append(R[:,8])
                tSZ_lens_1h.append(R[:,9])
                tSZ_lens_2h.append(R[:,10])
                isw_lens.append(R[:,11])
                isw_tsz.append(R[:,12])
                isw_auto.append(R[:,13])
                tSZ_gal_1h.append(R[:,20])
                tSZ_tSZ_tSZ_1h.append(R[:,21])
                gal_gal_1h.append(R[:,22])
                gal_gal_2h.append(R[:,23])
                # L = [multipole,cl_1h]
                # r_dict[p_val] = L

                #store value of Cl at ell=100
                if (args.compute_scaling_with_param == 'yes'):
                    x = np.log(multipoles[id_p])
                    y = np.log(cl_1h[id_p])
                    f = interpolate.interp1d(x, y)
                    cl_1h_100.append(np.exp(f(np.log(100.))))





                #ax.plot(x_axis,y_axis,color=next(colors),ls='-',alpha = 1.,label = val_label)
                verr = y_err[id_p]
                if (args.plot_trispectrum == 'yes'):
                    ax.plot(multipoles[id_p],trispectrum[id_p],color=col[id_p],ls='-.',alpha = 1.,label = val_label[id_p],marker='o')
                elif (args.plot_te_y_y == 'yes'):
                    print(te_y_y[id_p])
                    ax.plot(multipoles[id_p],te_y_y[id_p],color=col[id_p],ls='-.',alpha = 1.,label = val_label[id_p],marker='o')
                elif (args.plot_kSZ_kSZ_gal_1halo == 'yes'):
                    print(kSZ_kSZ_gal_1halo[id_p])
                    ax.plot(multipoles[id_p],kSZ_kSZ_gal_1halo[id_p],color=col[id_p],ls='-',alpha = 1.,label = val_label[id_p],marker='o')
                    ax.plot(multipoles[id_p],-kSZ_kSZ_gal_1halo[id_p],color=col[id_p],ls='--',alpha = 1.,marker='o')
                elif (args.plot_tSZ_tSZ_tSZ_1h == 'yes'):
                    print(tSZ_tSZ_tSZ_1h[id_p])
                    ax.plot(multipoles[id_p],tSZ_tSZ_tSZ_1h[id_p],color=col[id_p],ls='-',alpha = 1.,label = val_label[id_p],marker='o')
                    ax.plot(multipoles[id_p],-tSZ_tSZ_tSZ_1h[id_p],color=col[id_p],ls='--',alpha = 1.,marker='o')
                elif (args.plot_tSZ_lens == 'yes'):
                    print(tSZ_lens_1h[id_p])
                    print(tSZ_lens_2h[id_p])
                    #for (nu,colg) in zip((100,143,353),('k','r','b')):
                    for (nu,colg) in zip((100,353),('k','r')):
                        g = g_nu(nu)
                        print(g)
                        if g>0:
                            ax.plot(multipoles[id_p],g*tSZ_lens_1h[id_p]*Tcmb,color=colg,ls='-',alpha = 1.,label = '1-halo @ %.2f GHz'%nu)
                            ax.plot(multipoles[id_p],g*tSZ_lens_2h[id_p]*Tcmb,color='g',ls='-',alpha = 1.,label = '2-halo')
                            ax.plot(multipoles[id_p],g*(tSZ_lens_2h[id_p]+tSZ_lens_1h[id_p])*Tcmb,color=colg,ls=':',alpha = 1.,label = val_label[id_p])
                        else:
                            ax.plot(multipoles[id_p],-g*tSZ_lens_1h[id_p]*Tcmb,color=colg,ls='--',alpha = 1.,label='1-halo @ %.2f GHz'%nu)
                            ax.plot(multipoles[id_p],-g*tSZ_lens_2h[id_p]*Tcmb,color='g',ls='--',alpha = 1.,label='2-halo')
                            ax.plot(multipoles[id_p],-g*(tSZ_lens_2h[id_p]+tSZ_lens_1h[id_p])*Tcmb,color=colg,ls=':',alpha = 1.,label = val_label[id_p])
                elif (args.plot_tSZ_gal == 'yes'):
                    print(tSZ_gal_1h[id_p])
                    #print(tSZ_lens_2h[id_p])
                    #for (nu,colg) in zip((100,143,353),('k','r','b')):
                    fac = multipoles[id_p]*(multipoles[id_p]+1.)/2./np.pi*1e6
                    if (val_label[id_p] == 'green_shallow'):
                        ax.plot(multipoles[id_p],(tSZ_gal_1h[id_p])/fac,color='forestgreen',ls='--',alpha = 1.,label = val_label[id_p])
                    elif (val_label[id_p] == 'green'):
                        ax.plot(multipoles[id_p],(tSZ_gal_1h[id_p])/fac,color='green',ls='-',alpha = 1.,label = val_label[id_p])
                    elif (val_label[id_p] == 'blue'):
                        ax.plot(multipoles[id_p],(tSZ_gal_1h[id_p])/fac,color='blue',ls='-',alpha = 1.,label = val_label[id_p])
                    elif (val_label[id_p] == 'red'):
                        ax.plot(multipoles[id_p],(tSZ_gal_1h[id_p])/fac,color='red',ls='-',alpha = 1.,label = val_label[id_p])
                    else:
                        ax.plot(multipoles[id_p],(tSZ_gal_1h[id_p])/fac,color=col[id_p],ls='-',alpha = 1.,label = 'class_sz')
                    ax.plot(ell_KA20,cl_yg_1h_KA20,label='KA20')
                elif (args.plot_gal_gal == 'yes'):
                    print('plotting gxg')
                    fac = multipoles[id_p]*(multipoles[id_p]+1.)/2./np.pi
                    print(gal_gal_1h[id_p])
                    ax.plot(multipoles[id_p],(gal_gal_1h[id_p])/fac,color=col[id_p],ls='-',alpha = 1.,label = 'class_sz gg-1h')
                    ax.plot(ell_KA20,cl_gg_1h_KA20,label='KA20-1h')
                    ax.plot(multipoles[id_p],(gal_gal_2h[id_p])/fac,color=col[id_p],ls='--',alpha = 1.,label = 'class_sz gg-2h')
                    ax.plot(ell_KA20,cl_gg_2h_KA20,label='KA20-2h')

                    # for (nu,colg) in zip((100,353),('k','r')):
                    #     g = g_nu(nu)
                    #     print(g)
                    #     if g>0:
                    #         ax.plot(multipoles[id_p],(tSZ_gal_1h[id_p]),color=colg,ls='-',alpha = 1.,label = '1-halo')
                    #         #ax.plot(multipoles[id_p],g*tSZ_lens_2h[id_p]*Tcmb,color=colg,ls='-',alpha = 1.,label = '2-halo')
                    #         #ax.plot(multipoles[id_p],g*(tSZ_gal_2h[id_p]+tSZ_gal_1h[id_p])*Tcmb,color=colg,ls=':',alpha = 1.,label = val_label[id_p])
                    #     else:
                    #         #ax.plot(multipoles[id_p],-g*tSZ_lens_1h[id_p]*Tcmb,color=colg,ls='--',alpha = 1.,label='1-halo @ %.2f GHz'%nu)
                    #         #ax.plot(multipoles[id_p],-g*tSZ_lens_2h[id_p]*Tcmb,color=colg,ls='--',alpha = 1.,label='2-halo')
                    #         ax.plot(multipoles[id_p],(tSZ_gal_1h[id_p]),color=colg,ls=':',alpha = 1.,label = val_label[id_p])


                elif (args.plot_isw_lens == 'yes'):
                    print(isw_lens[id_p])
                    ax.plot(multipoles[id_p],isw_lens[id_p],color=col[id_p],ls='-',alpha = 1.,label = val_label[id_p])
                    ax.plot(multipoles[id_p],-isw_lens[id_p],color=col[id_p],ls='--',alpha = 1.)
                    class_cls = np.loadtxt(path_to_class+'sz_auxiliary_files/run_scripts/tmp/class-sz_tmp_cl.dat')
                    ax.plot(class_cls[:,0],class_cls[:,3],ls=':',c=col[id_p],label = 'Cl^isw-lens class')

                elif (args.plot_isw_tsz == 'yes'):
                    print(isw_tsz[id_p])
                    ax.plot(multipoles[id_p],isw_tsz[id_p],color=col[id_p],ls='-',alpha = 1.,label = 'Cl^isw-y class_sz %s'%(val_label[id_p]))
                    ax.plot(multipoles[id_p],-isw_tsz[id_p],color=col[id_p],ls='--',alpha = 1.)
                elif (args.plot_isw_auto == 'yes'):
                    print(isw_auto[id_p])
                    ax.plot(multipoles[id_p],isw_auto[id_p],color=col[id_p],ls='-',alpha = 1.,label = 'Cl^isw-isw class_sz %s'%(val_label[id_p]),marker='o',markersize=1)
                    ax.plot(multipoles[id_p],-isw_auto[id_p],color=col[id_p],ls='--',alpha = 1.)
                    if ('tCl' in p_dict['output']):
                        class_cls = np.loadtxt(path_to_class+'sz_auxiliary_files/run_scripts/tmp/class-sz_tmp_cl.dat')
                        ax.plot(class_cls[:,0],class_cls[:,1],ls='-',c='r',label = 'Cl^isw-isw class %s'%(val_label[id_p]))
                else:
                    if ('tSZ_1h' in p_dict['output']):
                        if (args.show_error_bars == 'yes'):
                            ax.errorbar(multipoles[id_p],cl_1h[id_p],yerr=[verr,verr],color=col[id_p],ls='-.',alpha = 1.,label = val_label[id_p])
                        else:
                            #ax.plot(multipoles[id_p],cl_1h[id_p],color=col[id_p],ls='-',alpha = 1.,label = val_label[id_p])
                            ax.plot(multipoles[id_p],cl_1h[id_p],color='r',ls='-',alpha = 1.,label = 'Cl^1h [A10,T10]')
                    if ('tSZ_2h' in p_dict['output']):
                        #print(cl_2h[id_p])
                        #ax.plot(multipoles[id_p],cl_2h[id_p],color=col[id_p],ls='-',label = val_label[id_p])
                        #ax.plot(multipoles[id_p],cl_2h[id_p],color=col[id_p],ls='-.',label = 'Cl^2h class_sz')
                        ax.plot(multipoles[id_p],cl_2h[id_p],color='r',ls='--',label = 'Cl^2h [A10,T10]')

            plt.draw()
            plt.pause(0.05)

            id_p += 1

        #end loop on p over param values

        if ('hmf' in p_dict['output']):
            #HMF = 3.046174198e-4*41253.0*np.loadtxt(path_to_class+'sz_auxiliary_files/run_scripts/tmp/class-sz_tmp_hmf_int.txt')
            HMF = np.loadtxt(path_to_class+'sz_auxiliary_files/run_scripts/tmp/class-sz_tmp_hmf_int.txt')
            print("(nb) Full-sky  N_tot = %.10e"%HMF[1])
        if ('mean_y' in p_dict['output']):
            mean_y = np.loadtxt(path_to_class+'sz_auxiliary_files/run_scripts/tmp/class-sz_tmp_mean_y.txt')
            print("(nb) y_mean = %.10e"%mean_y)

        if (args.plot_ref_data == 'yes' and args.plot_isw_tsz == 'yes'):
            LC = np.loadtxt('/Users/boris/Work/CLASS-SZ/SO-SZ/class_sz/sz_auxiliary_files/chill_cl-isw_y.txt')
            multipoles_ref = LC[:,0]
            cl_1h_ref = LC[:,1]*LC[:,0]*(LC[:,0]+1.)/2./np.pi
            ax.plot(multipoles_ref,cl_1h_ref,color='k',ls='--',alpha = 1.,label='Cl^isw-y hill')
            LC = np.loadtxt('/Users/boris/Work/CLASS-SZ/SO-SZ/class_sz/sz_auxiliary_files/cs2016_cl-isw_y.txt')
            multipoles_ref = LC[:,0]
            cl_1h_ref = LC[:,1]
            ax.plot(multipoles_ref,cl_1h_ref,color='green',ls='--',alpha = 1.,label='Cl^isw-y cs16')
            plt.draw()
        if (args.plot_ref_data == 'yes' and args.plot_isw_auto == 'yes'):
            LC = np.loadtxt('/Users/boris/Work/CLASS-SZ/SO-SZ/class_sz/sz_auxiliary_files/chill_cl-isw_y.txt')
            multipoles_ref = LC[:,0]
            cl_1h_ref = LC[:,2]*LC[:,0]*(LC[:,0]+1.)/2./np.pi
            ax.plot(multipoles_ref,cl_1h_ref,color='k',ls='--',alpha = 1.,label='Cl^isw-isw hill')
            plt.draw()
        if ('tSZ_1h' in p_dict['output']):
            if(args.compute_scaling_with_param == 'yes'):
                ln_cl = np.log(np.asarray(cl_1h_100))
                #if (param_name == 'HSEbias'):
                #     ln_p = np.log(1./(1.-p)) #if HSEbias
                # else:
                ln_p = np.log(p)
                slope, intercept, r_value, p_value, std_err = stats.linregress(ln_p,ln_cl)
                print("slope = %.4e,\t intercept = %.4e\n"%(slope,intercept))


            if(args.plot_ref_data == 'yes' and not args.plot_redshift_dependent_functions == 'yes'):
                #L = np.loadtxt('/Users/boris/Work/CLASS-SZ/SO-SZ/class_sz/sz_auxiliary_files/chill_cltsz_data.txt')
                #L_ref = np.loadtxt('/Users/boris/Work/CLASS-SZ/SO-SZ/class_sz/output/class-sz_tmp_szpowerspectrum_patterson.txt')
                # L_ref = np.loadtxt('/Users/boris/Work/CLASS-SZ/SO-SZ/class_sz/output/class-sz_tmp_szpowerspectrum_mnu_0d02_ref.txt')

                L_ref = np.loadtxt(path_to_class + '/sz_auxiliary_files/class-sz_B12_rotti++20_szpowerspectrum.txt')
                multipoles_ref = L_ref[:,0]
                cl_1h_ref = L_ref[:,1]
                trispectrum_ref = L_ref[:,3]
                cl_2h_ref = L_ref[:,6]

                # #LC = np.loadtxt('/Users/boris/Work/CLASS-SZ/SO-SZ/class_sz/sz_auxiliary_files/chill_cltsz_data_P13.txt')
                # LC = np.loadtxt('/Users/boris/Work/CLASS-SZ/SO-SZ/class_sz/sz_auxiliary_files/chill_cltsz_data_B12.txt')
                # # LC = np.loadtxt('/Users/boris/Work/CLASS-SZ/SO-SZ/class_sz/sz_auxiliary_files/chill_cltsz_data_A10.txt')
                # multipoles_ref = LC[:,0]
                # cl_1h_ref = 1.e12*LC[:,9]*LC[:,0]*(LC[:,0]+1.)/2./np.pi
                # cl_2h_ref = 1.e12*LC[:,10]*LC[:,0]*(LC[:,0]+1.)/2./np.pi

                if (args.plot_trispectrum == 'yes'):
                    ax.plot(multipoles_ref,trispectrum_ref,c='k',ls='--',label='ref',alpha=0.7)
                else :
                    if ('tSZ_1h' in p_dict['output']):
                        if (args.show_error_bars == 'yes'):
                            verr = L_ref[:,5]/np.sqrt(f_sky)
                            ax.errorbar(multipoles_ref,cl_1h_ref,yerr=[verr,verr],color='k',ls='--',alpha = 0.5,label='Cl^1h ref')
                        else:
                            ax.plot(multipoles_ref,cl_1h_ref,color='k',ls='-',alpha = 1.,label='Cl^1h [B12,T10]')
                    if ('tSZ_2h' in p_dict['output']):
                        #print(cl_2h_ref)
                        ax.plot(multipoles_ref,cl_2h_ref,color='k',ls='--',label='Cl^2h [B12,T10]')
                        #ax.plot(multipoles_ref,cl_2h_ref,color='k',ls='--',label='Cl^2h ref')

                plt.draw()




                #
                # LC = np.loadtxt('/Users/boris/Work/CLASS-SZ/code_comparison/szfastdks/multipole_szpower_150ghz_colin_params.txt')
                # multipoles_ref = LC[:,0]
                # cl_1h_ref = LC[:,1]
                # ax.plot(multipoles_ref,cl_1h_ref/2.598296e+00**2,color='blue',ls='--',alpha = 1.,label='Cl^1h szfast')


                #ax.plot(multipoles_ref,cl_1h_ref,c='k',ls='--',label='Cl^1h ref',alpha=0.7)
            #plt.draw()
            #plt.plot(L[:,0],1.e12*L[:,10]*L[:,0]*(L[:,0]+1.)/2./np.pi,c='k',ls='-',label='Cl^2h colin')
            if(args.print_rel_diff=='yes'):
                # x = np.log(multipoles[0])
                # y = np.log(cl_1h[0])
                # f = interpolate.interp1d(x, y)
                # x_new = np.log(multipoles_ref)
                # cl_new = np.exp(f(x_new))
                # rel_diff = (cl_new-cl_1h_ref)/cl_1h_ref
                # for (ell,rdiff) in zip(multipoles_ref,rel_diff):
                #     print("ell = %.4e\t rel_diff = %.4e\n"%(ell,rdiff))
                ax = ax2
                ax.tick_params(axis = 'x',which='both',length=5,direction='in', pad=10)
                ax.tick_params(axis = 'y',which='both',length=5,direction='in', pad=5)
                ax.xaxis.set_ticks_position('both')
                ax.yaxis.set_ticks_position('both')
                plt.setp(ax.get_yticklabels(), rotation='horizontal', fontsize=label_size)
                plt.setp(ax.get_xticklabels(), fontsize=label_size)
                ax.grid( b=True, which="both", alpha=0.3, linestyle='--')
                ax.set_xscale('log')
                ax.set_yscale('linear')
                ax.set_xlabel(r'$\ell$',size=title_size)
                #ax.set_ylabel(r'$[\mathrm{C^{tSZ}_\ell-C^{tSZ,ref}_\ell}]/\mathrm{C^{tSZ,ref}_\ell}}$',size=title_size)
                ax.set_ylabel(r'$\Delta\mathrm{C^{yy}_\ell}/\mathrm{C^{yy}_\ell}$',size=title_size)

                id_p = 0
                for p_val in p:
                    x = np.log(multipoles[id_p])
                    y = np.log(cl_1h[id_p])
                    f = interpolate.interp1d(x, y)
                    x_new = np.log(multipoles_ref)
                    cl_new = np.exp(f(x_new))
                    rel_diff = (cl_new-cl_1h_ref)/cl_1h_ref
                    for (ell,rdiff) in zip(multipoles_ref,rel_diff):
                        print("ell = %.4e\t rel_diff = %.4e\n"%(ell,rdiff))

                    #ax.plot(multipoles_ref,rel_diff,color=col[id_p],ls='-',alpha = 1.,label = val_label[id_p])
                    ax.plot(multipoles_ref,rel_diff,color=col[id_p],ls='-',alpha = 1.,label = '1-halo')

                    if ('tSZ_2h' in p_dict['output']):
                        y = np.log(cl_2h[id_p])
                        f = interpolate.interp1d(x, y)
                        x_new = np.log(multipoles_ref)
                        cl_new = np.exp(f(x_new))
                        rel_diff = (cl_new-cl_2h_ref)/cl_2h_ref
                        for (ell,rdiff) in zip(multipoles_ref,rel_diff):
                            print("ell = %.4e\t rel_diff_2h = %.4e\n"%(ell,rdiff))

                        ax.plot(multipoles_ref,rel_diff,color=col[id_p],ls='-.',alpha = 1.,label = '2-halo')
                    #plt.draw()
                    #plt.pause(0.05)
                    id_p += 1


                # L = np.loadtxt('/Users/boris/Work/CLASS-SZ/SO-SZ/class_sz/output/class-compare_with_colin_07022020_1d5r200c_szpowerspectrum.txt')
                # plt.plot(L[:,0],L[:,1],ls='-.',c='g',label='Cl^1h boris 1d5r200c')
                # plt.plot(L[:,0],L[:,6],ls='-.',c='g',label='Cl^2h boris 1d5r200c')





            #save some results and remove the temporary files
            if (args.save_tsz_ps == 'yes'):
                subprocess.call(['cp',path_to_class+'sz_auxiliary_files/run_scripts/tmp/class-sz_tmp_szpowerspectrum.txt', path_to_class+'output/'])


    if (args.show_legend == 'yes'):
        if (args.plot_isw_tsz == 'yes' or args.plot_isw_auto == 'yes'):
            ax1.legend(loc=1)
        elif (args.plot_tSZ_lens == 'yes' or args.plot_isw_lens == 'yes'  or args.plot_tSZ_gal == 'yes'):
            ax1.legend(loc=3,ncol = 2)
        else:
            ax1.legend(loc=2)
        if (args.print_rel_diff == 'yes'):
            ax2.legend(loc=1,ncol = 1)
        else:
            ax1.legend(loc=3,ncol = 2)


    fig.tight_layout()


    if (args.save_fig == 'yes'):
        FIG_NAME = '/tSZ_varying_' + param_name
        plt.savefig(FIG_DIR + FIG_NAME +".pdf")

    plt.show(block=True)






        #subprocess.call(['rm','-r',path_to_class+'sz_auxiliary_files/run_scripts/tmp'])









def main():
    parser=argparse.ArgumentParser(description="Plot cosmotherm spectra")
    parser.add_argument("-param_name",help="name of varying parameter" ,dest="param_name", type=str, required=True)
    parser.add_argument("-min",help="minimum value of parameter" ,dest="p_min", type=str, required=False)
    parser.add_argument("-max",help="maximum value of parameter" ,dest="p_max", type=str, required=False)
    parser.add_argument("-N",help="number of evaluations" ,dest="N", type=int, required=False)
    parser.add_argument("-p_val",help="list of param values" ,dest="p_val", type=str, required=False)
    parser.add_argument("-spacing",help="linear (lin) or log spacing (log)" ,dest="spacing", type=str, required=False)
    parser.add_argument("-show_legend",help="show legend on figure? ('yes' or 'no')" ,dest="show_legend", type=str, required=True)
    parser.add_argument("-show_error_bars",help="show error bars on figure? ('yes' or 'no')" ,dest="show_error_bars", type=str, required=True)
    parser.add_argument("-y_min",help="ylim for y-axis" ,dest="y_min", type=str, required=False)
    parser.add_argument("-y_max",help="ylim for y-axis" ,dest="y_max", type=str, required=False)
    parser.add_argument("-f_sky",help="sky fraction f_sky" ,dest="f_sky", type=str, required=False)
    parser.add_argument("-output",help="what quantities to plot" ,dest="output", type=str, required=False)
    parser.add_argument("-plot_ref_data",help="some other spectra" ,dest="plot_ref_data", type=str, required=False)
    parser.add_argument("-compute_scaling_with_param",help="Compute alpha in C_l ~ p^alpha at l=100" ,dest="compute_scaling_with_param", type=str, required=False)
    parser.add_argument("-save_tsz_ps",help="save file with tsz power spectrum in output directory" ,dest="save_tsz_ps", type=str, required=False)
    parser.add_argument("-save_figure",help="save figure" ,dest="save_fig", type=str, required=False)
    parser.add_argument("-print_rel_diff",help="[cl-cl_ref]/cl_ref" ,dest="print_rel_diff", type=str, required=False)
    parser.add_argument("-plot_trispectrum",help="Tll" ,dest="plot_trispectrum", type=str, required=False)
    parser.add_argument("-plot_te_y_y",help="Tll" ,dest="plot_te_y_y", type=str, required=False)
    parser.add_argument("-plot_kSZ_kSZ_gal_1halo",help="kSZ_kSZ_gal_1halo" ,dest="plot_kSZ_kSZ_gal_1halo", type=str, required=False)
    parser.add_argument("-plot_tSZ_tSZ_tSZ_1h",help="tSZ_tSZ_tSZ_1h" ,dest="plot_tSZ_tSZ_tSZ_1h", type=str, required=False)
    parser.add_argument("-plot_tSZ_lens",help="tSZ_lens" ,dest="plot_tSZ_lens", type=str, required=False)
    parser.add_argument("-plot_tSZ_gal",help="tSZ_gal" ,dest="plot_tSZ_gal", type=str, required=False)
    parser.add_argument("-plot_gal_gal",help="gal_gal" ,dest="plot_gal_gal", type=str, required=False)
    parser.add_argument("-plot_isw_lens",help="isw_lens" ,dest="plot_isw_lens", type=str, required=False)
    parser.add_argument("-plot_isw_tsz",help="isw_tsz" ,dest="plot_isw_tsz", type=str, required=False)
    parser.add_argument("-plot_isw_auto",help="isw_auto" ,dest="plot_isw_auto", type=str, required=False)
    parser.add_argument("-plot_redshift_dependent_functions",help="redshift dependent functions" ,dest="plot_redshift_dependent_functions", type=str, required=False)
    parser.set_defaults(func=run)
    args=parser.parse_args()
    args.func(args)

if __name__=="__main__":
	main()