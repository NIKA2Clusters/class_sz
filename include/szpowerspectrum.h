/** @file szpowerspectrum.h Documented includes for sz module. */
#ifndef __SZ__
#define __SZ__

#include "common.h"
#include "lensing.h"
#include "gsl/gsl_integration.h"
#include "gsl/gsl_sf_erf.h"
#include "gsl/gsl_sf_expint.h"
#include "gsl/gsl_sf_lambert.h"


#define _pk_at_z_1h_ ((ptsz->has_pk_at_z_1h == _TRUE_) && (index_md == ptsz->index_md_pk_at_z_1h))
#define _pk_at_z_2h_ ((ptsz->has_pk_at_z_2h == _TRUE_) && (index_md == ptsz->index_md_pk_at_z_2h))
#define _mean_y_ ((ptsz->has_mean_y == _TRUE_) && (index_md == ptsz->index_md_mean_y))
#define _hmf_ ((ptsz->has_hmf == _TRUE_) && (index_md == ptsz->index_md_hmf))
#define _tSZ_power_spectrum_ ((ptsz->has_sz_ps == _TRUE_) && (index_md == ptsz->index_md_sz_ps))
#define _trispectrum_ ((ptsz->has_sz_trispec == _TRUE_) && (index_md == ptsz->index_md_trispectrum))
#define _2halo_ ((ptsz->has_sz_2halo == _TRUE_) && (index_md == ptsz->index_md_2halo))
#define _te_y_y_ ((ptsz->has_sz_te_y_y == _TRUE_) && (index_md == ptsz->index_md_te_y_y))
#define _m_y_y_1h_ ((ptsz->has_sz_m_y_y_1h == _TRUE_) && (index_md == ptsz->index_md_m_y_y_1h))
#define _m_y_y_2h_ ((ptsz->has_sz_m_y_y_2h == _TRUE_) && (index_md == ptsz->index_md_m_y_y_2h))
#define _cov_Y_N_ ((ptsz->has_sz_cov_Y_N == _TRUE_) && (index_md == ptsz->index_md_cov_Y_N))
#define _cov_N_N_ ((ptsz->has_sz_cov_N_N == _TRUE_) && (index_md == ptsz->index_md_cov_N_N))
#define _cov_N_N_hsv_ ((ptsz->has_sz_cov_N_N_hsv == _TRUE_) && (index_md == ptsz->index_md_cov_N_N_hsv))
#define _cov_Y_Y_ssc_ ((ptsz->has_sz_cov_Y_Y_ssc == _TRUE_) && (index_md == ptsz->index_md_cov_Y_Y_ssc))
#define _cov_Y_N_next_order_ ((ptsz->has_sz_cov_Y_N_next_order == _TRUE_) && (index_md == ptsz->index_md_cov_Y_N_next_order))
#define _kSZ_kSZ_gal_1h_ ((ptsz->has_kSZ_kSZ_gal_1h == _TRUE_) && (index_md == ptsz->index_md_kSZ_kSZ_gal_1h))
#define _kSZ_kSZ_gal_2h_ ((ptsz->has_kSZ_kSZ_gal_2h == _TRUE_) && (index_md == ptsz->index_md_kSZ_kSZ_gal_2h))
#define _kSZ_kSZ_gal_3h_ ((ptsz->has_kSZ_kSZ_gal_3h == _TRUE_) && (index_md == ptsz->index_md_kSZ_kSZ_gal_3h))
#define _kSZ_kSZ_lensmag_1halo_ ((ptsz->has_kSZ_kSZ_lensmag_1halo == _TRUE_) && (index_md == ptsz->index_md_kSZ_kSZ_lensmag_1halo))
#define _gal_gal_1h_ ((ptsz->has_gal_gal_1h == _TRUE_) && (index_md == ptsz->index_md_gal_gal_1h))
#define _gal_gal_2h_ ((ptsz->has_gal_gal_2h == _TRUE_) && (index_md == ptsz->index_md_gal_gal_2h))
#define _gal_lens_2h_ ((ptsz->has_gal_lens_2h == _TRUE_) && (index_md == ptsz->index_md_gal_lens_2h))
#define _gal_lens_1h_ ((ptsz->has_gal_lens_1h == _TRUE_) && (index_md == ptsz->index_md_gal_lens_1h))
#define _gal_lensmag_2h_ ((ptsz->has_gal_lensmag_2h == _TRUE_) && (index_md == ptsz->index_md_gal_lensmag_2h))
#define _gal_lensmag_1h_ ((ptsz->has_gal_lensmag_1h == _TRUE_) && (index_md == ptsz->index_md_gal_lensmag_1h))
#define _lensmag_lensmag_2h_ ((ptsz->has_lensmag_lensmag_2h == _TRUE_) && (index_md == ptsz->index_md_lensmag_lensmag_2h))
#define _lensmag_lensmag_1h_ ((ptsz->has_lensmag_lensmag_1h == _TRUE_) && (index_md == ptsz->index_md_lensmag_lensmag_1h))
#define _lens_lensmag_2h_ ((ptsz->has_lens_lensmag_2h == _TRUE_) && (index_md == ptsz->index_md_lens_lensmag_2h))
#define _lens_lensmag_1h_ ((ptsz->has_lens_lensmag_1h == _TRUE_) && (index_md == ptsz->index_md_lens_lensmag_1h))
#define _lens_lens_1h_ ((ptsz->has_lens_lens_1h == _TRUE_) && (index_md == ptsz->index_md_lens_lens_1h))
#define _lens_lens_2h_ ((ptsz->has_lens_lens_2h == _TRUE_) && (index_md == ptsz->index_md_lens_lens_2h))
#define _tSZ_gal_1h_ ((ptsz->has_tSZ_gal_1h == _TRUE_) && (index_md == ptsz->index_md_tSZ_gal_1h))
#define _tSZ_gal_2h_ ((ptsz->has_tSZ_gal_2h == _TRUE_) && (index_md == ptsz->index_md_tSZ_gal_2h))
#define _tSZ_cib_1h_ ((ptsz->has_tSZ_cib_1h == _TRUE_) && (index_md == ptsz->index_md_tSZ_cib_1h))
#define _tSZ_cib_2h_ ((ptsz->has_tSZ_cib_2h == _TRUE_) && (index_md == ptsz->index_md_tSZ_cib_2h))
#define _cib_cib_1h_ ((ptsz->has_cib_cib_1h == _TRUE_) && (index_md == ptsz->index_md_cib_cib_1h))
#define _cib_cib_2h_ ((ptsz->has_cib_cib_2h == _TRUE_) && (index_md == ptsz->index_md_cib_cib_2h))
#define _lens_cib_1h_ ((ptsz->has_lens_cib_1h == _TRUE_) && (index_md == ptsz->index_md_lens_cib_1h))
#define _lens_cib_2h_ ((ptsz->has_lens_cib_2h == _TRUE_) && (index_md == ptsz->index_md_lens_cib_2h))
#define _tSZ_lens_1h_ ((ptsz->has_tSZ_lens_1h == _TRUE_) && (index_md == ptsz->index_md_tSZ_lens_1h))
#define _tSZ_lens_2h_ ((ptsz->has_tSZ_lens_2h == _TRUE_) && (index_md == ptsz->index_md_tSZ_lens_2h))
#define _isw_lens_ ((ptsz->has_isw_lens == _TRUE_) && (index_md == ptsz->index_md_isw_lens))
#define _isw_tsz_ ((ptsz->has_isw_tsz == _TRUE_) && (index_md == ptsz->index_md_isw_tsz))
#define _isw_auto_ ((ptsz->has_isw_auto == _TRUE_) && (index_md == ptsz->index_md_isw_auto))
#define _dndlnM_ ((ptsz->has_dndlnM == _TRUE_) && (index_md == ptsz->index_md_dndlnM))
#define _tSZ_tSZ_tSZ_1halo_ ((ptsz->has_tSZ_tSZ_tSZ_1halo == _TRUE_) && (index_md == ptsz->index_md_tSZ_tSZ_tSZ_1halo))

//#define _tSZ_trispectrum_ ((ptsz->has_sz_trispec == _TRUE_))
//#define _tSZ_2halo_ ((ptsz->has_sz_2halo == _TRUE_))
//#define _tSZ_te_y_y_ ((ptsz->has_sz_te_y_y == _TRUE_))
#define _cov_N_Cl_ ((ptsz->has_sz_cov_N_Cl == _TRUE_))





struct tszspectrum {



  #define __ALLOCATE_TSZ_PARAMETER__
  #include "class_sz_precisions.h"
  #undef __ALLOCATE_TSZ_PARAMETER__



  int use_analytical_truncated_nfw;
  int use_hod; // Eq. 15 or 16 of KA20
  int unwise_galaxy_sample_id;
  int galaxy_sample;
  //double unwise_m_min_cut;

  double sn_cutoff;

  double f_sky;
  double Omega_survey;

  double chi_star; //comoving distance to the surface of last scattering [Mpc/h]

  double hmf_int;
  double y_monopole;
  double * pk_at_z_1h;
  double * pk_at_z_2h;
  double * cl_sz_1h;
  double * cl_gal_gal_1h;
  double * cl_gal_gal_2h;
  double * cl_gal_lens_2h;
  double * cl_gal_lens_1h;
  double * cl_gal_lensmag_2h;
  double * cl_gal_lensmag_1h;
  double * cl_lensmag_lensmag_2h;
  double * cl_lensmag_lensmag_1h;
  double * cl_lens_lensmag_2h;
  double * cl_lens_lensmag_1h;
  double * cl_lens_lens_1h;
  double * cl_lens_lens_2h;
  double * cl_tSZ_gal_1h;
  double * cl_tSZ_gal_2h;
  double *** cl_cib_cib_1h;
  double *** cl_cib_cib_2h;
  double ** cl_tSZ_cib_1h;
  double ** cl_tSZ_cib_2h;
  double ** cl_lens_cib_1h;
  double ** cl_lens_cib_2h;
  double * cl_tSZ_lens_1h;
  double * cl_tSZ_lens_2h;
  double * cl_isw_lens;
  double * cl_isw_tsz;
  double * cl_isw_auto;
  double * cl_kSZ_kSZ_gal_1h;
  double * cl_kSZ_kSZ_gal_2h;
  double * cl_kSZ_kSZ_gal_3h;
  double * cl_kSZ_kSZ_lensmag_1h;
  double * b_tSZ_tSZ_tSZ_1halo;
  double * cl_te_y_y;
  double * m_y_y_1h;
  double * m_y_y_2h;
  double ** tllprime_sz;
  double ** dndlnM_at_z_and_M;
  double * cl_sz_2h;
  double ** cov_N_cl;
  double ** r_N_cl;
  double ** cov_Y_N;
  double ** cov_Y_N_next_order;
  double ** cov_Y_Y_ssc;
  double * cov_N_N;
  double ** cov_N_N_hsv;
  double ** r_Y_N;
  double ** r_cl_clp;
  double ** trispectrum_ref;
  double * cov_cl_cl;
  double * sig_cl_squared_binned;

  int index_md;

  int has_sz_counts;

  int create_ref_trispectrum_for_cobaya;


  //int has_sz_te_y_y;
  int has_sz_cov_N_Cl;

  int has_sz_cov_Y_N;
  int index_md_cov_Y_N;
  int index_integrand_id_cov_Y_N_first;
  int index_integrand_id_cov_Y_N_last;

  int has_sz_cov_Y_N_next_order;
  int index_md_cov_Y_N_next_order;
  int index_integrand_id_cov_Y_N_next_order_first;
  int index_integrand_id_cov_Y_N_next_order_last;

  int has_sz_cov_Y_Y_ssc;
  int index_md_cov_Y_Y_ssc;
  int index_integrand_id_cov_Y_Y_ssc_first;
  int index_integrand_id_cov_Y_Y_ssc_last;

  int has_sz_cov_N_N;
  int index_md_cov_N_N;
  int index_integrand_id_cov_N_N_first;
  int index_integrand_id_cov_N_N_last;

  int has_sz_cov_N_N_hsv;
  int index_md_cov_N_N_hsv;
  int index_integrand_id_cov_N_N_hsv_first;
  int index_integrand_id_cov_N_N_hsv_last;


  int has_hmf;
  int index_md_hmf;
  int index_integrand_id_hmf;

  int has_pk_at_z_1h;
  int index_md_pk_at_z_1h;
  int index_integrand_id_pk_at_z_1h_first;
  int index_integrand_id_pk_at_z_1h_last;

  int has_pk_at_z_2h;
  int index_md_pk_at_z_2h;
  int index_integrand_id_pk_at_z_2h_first;
  int index_integrand_id_pk_at_z_2h_last;


  int has_mean_y;
  int index_md_mean_y;
  int index_integrand_id_mean_y;

  int has_sz_ps;
  int index_md_sz_ps;
  int index_integrand_id_sz_ps_first;
  int index_integrand_id_sz_ps_last;

  int has_sz_2halo;
  int index_md_2halo;
  int index_integrand_id_sz_ps_2halo_first;
  int index_integrand_id_sz_ps_2halo_last;

  int has_sz_te_y_y;
  int index_md_te_y_y;
  int index_integrand_id_sz_ps_te_y_y_first;
  int index_integrand_id_sz_ps_te_y_y_last;

  int has_sz_m_y_y_1h;
  int index_md_m_y_y_1h;
  int index_integrand_id_sz_ps_m_y_y_1h_first;
  int index_integrand_id_sz_ps_m_y_y_1h_last;

  int has_sz_m_y_y_2h;
  int index_md_m_y_y_2h;
  int index_integrand_id_sz_ps_m_y_y_2h_first;
  int index_integrand_id_sz_ps_m_y_y_2h_last;

  int has_kSZ_kSZ_gal_1h;
  int index_md_kSZ_kSZ_gal_1h;
  int index_integrand_id_kSZ_kSZ_gal_1h_first;
  int index_integrand_id_kSZ_kSZ_gal_1h_last;

  int has_kSZ_kSZ_gal_2h;
  int index_md_kSZ_kSZ_gal_2h;
  int index_integrand_id_kSZ_kSZ_gal_2h_first;
  int index_integrand_id_kSZ_kSZ_gal_2h_last;

  int has_kSZ_kSZ_gal_3h;
  int index_md_kSZ_kSZ_gal_3h;
  int index_integrand_id_kSZ_kSZ_gal_3h_first;
  int index_integrand_id_kSZ_kSZ_gal_3h_last;


  int has_kSZ_kSZ_lensmag_1halo;
  int index_md_kSZ_kSZ_lensmag_1halo;
  int index_integrand_id_kSZ_kSZ_lensmag_1halo_first;
  int index_integrand_id_kSZ_kSZ_lensmag_1halo_last;


  int has_tSZ_tSZ_tSZ_1halo;
  int index_md_tSZ_tSZ_tSZ_1halo;
  int index_integrand_id_tSZ_tSZ_tSZ_1halo_first;
  int index_integrand_id_tSZ_tSZ_tSZ_1halo_last;

  int has_tSZ_lens_1h;
  int index_md_tSZ_lens_1h;
  int index_integrand_id_tSZ_lens_1h_first;
  int index_integrand_id_tSZ_lens_1h_last;

  int has_gal_gal_1h;
  int index_md_gal_gal_1h;
  int index_integrand_id_gal_gal_1h_first;
  int index_integrand_id_gal_gal_1h_last;

  int has_gal_gal_2h;
  int index_md_gal_gal_2h;
  int index_integrand_id_gal_gal_2h_first;
  int index_integrand_id_gal_gal_2h_last;

  int has_gal_lens_2h;
  int index_md_gal_lens_2h;
  int index_integrand_id_gal_lens_2h_first;
  int index_integrand_id_gal_lens_2h_last;

  int has_gal_lens_1h;
  int index_md_gal_lens_1h;
  int index_integrand_id_gal_lens_1h_first;
  int index_integrand_id_gal_lens_1h_last;

  int has_gal_lensmag_2h;
  int index_md_gal_lensmag_2h;
  int index_integrand_id_gal_lensmag_2h_first;
  int index_integrand_id_gal_lensmag_2h_last;

  int has_gal_lensmag_1h;
  int index_md_gal_lensmag_1h;
  int index_integrand_id_gal_lensmag_1h_first;
  int index_integrand_id_gal_lensmag_1h_last;


  int has_lensmag_lensmag_2h;
  int index_md_lensmag_lensmag_2h;
  int index_integrand_id_lensmag_lensmag_2h_first;
  int index_integrand_id_lensmag_lensmag_2h_last;

  int has_lensmag_lensmag_1h;
  int index_md_lensmag_lensmag_1h;
  int index_integrand_id_lensmag_lensmag_1h_first;
  int index_integrand_id_lensmag_lensmag_1h_last;


  int has_lens_lensmag_2h;
  int index_md_lens_lensmag_2h;
  int index_integrand_id_lens_lensmag_2h_first;
  int index_integrand_id_lens_lensmag_2h_last;

  int has_lens_lensmag_1h;
  int index_md_lens_lensmag_1h;
  int index_integrand_id_lens_lensmag_1h_first;
  int index_integrand_id_lens_lensmag_1h_last;

  int has_lens_lens_1h;
  int index_md_lens_lens_1h;
  int index_integrand_id_lens_lens_1h_first;
  int index_integrand_id_lens_lens_1h_last;

  int has_lens_lens_2h;
  int index_md_lens_lens_2h;
  int index_integrand_id_lens_lens_2h_first;
  int index_integrand_id_lens_lens_2h_last;

  int has_tSZ_gal_1h;
  int index_md_tSZ_gal_1h;
  int index_integrand_id_tSZ_gal_1h_first;
  int index_integrand_id_tSZ_gal_1h_last;

  int has_tSZ_gal_2h;
  int index_md_tSZ_gal_2h;
  int index_integrand_id_tSZ_gal_2h_first;
  int index_integrand_id_tSZ_gal_2h_last;

  int has_tSZ_cib_1h;
  int index_md_tSZ_cib_1h;
  int index_integrand_id_tSZ_cib_1h_first;
  int index_integrand_id_tSZ_cib_1h_last;

  int has_tSZ_cib_2h;
  int index_md_tSZ_cib_2h;
  int index_integrand_id_tSZ_cib_2h_first;
  int index_integrand_id_tSZ_cib_2h_last;

  int has_lens_cib_1h;
  int index_md_lens_cib_1h;
  int index_integrand_id_lens_cib_1h_first;
  int index_integrand_id_lens_cib_1h_last;

  int has_lens_cib_2h;
  int index_md_lens_cib_2h;
  int index_integrand_id_lens_cib_2h_first;
  int index_integrand_id_lens_cib_2h_last;

  int has_cib_cib_1h;
  int index_md_cib_cib_1h;
  int index_integrand_id_cib_cib_1h_first;
  int index_integrand_id_cib_cib_1h_last;

  int has_cib_cib_2h;
  int index_md_cib_cib_2h;
  int index_integrand_id_cib_cib_2h_first;
  int index_integrand_id_cib_cib_2h_last;

  int has_tSZ_lens_2h;
  int index_md_tSZ_lens_2h;
  int index_integrand_id_tSZ_lens_2h_first;
  int index_integrand_id_tSZ_lens_2h_last;

  int has_isw_lens;
  int index_md_isw_lens;
  int index_integrand_id_isw_lens_first;
  int index_integrand_id_isw_lens_last;

  int has_isw_tsz;
  int index_md_isw_tsz;
  int index_integrand_id_isw_tsz_first;
  int index_integrand_id_isw_tsz_last;

  int has_isw_auto;
  int index_md_isw_auto;
  int index_integrand_id_isw_auto_first;
  int index_integrand_id_isw_auto_last;


  int has_dndlnM;
  int index_md_dndlnM;
  int index_integrand_id_dndlnM_first;
  int index_integrand_id_dndlnM_last;

  int has_sz_trispec;
  //int index_md_sz_trispec;
  int index_integrand_id_trispectrum_first;
  int index_integrand_id_trispectrum_last;
  int index_md_trispectrum;


  int number_of_integrands;
  int index_integrand;
  int index_integrand_te_y_y;
  int index_integrand_2halo_term;

  int index_integrand_trispectrum_first; //for trispectrum
  int index_integrand_trispectrum_last;  //for trispectrum

  int index_integrand_cov_N_cl_first;
  int index_integrand_cov_N_cl_last;


  int index_integrand_N_for_cov_N_cl_first;
  int index_integrand_N_for_cov_N_cl_last;


  int index_integrand_id;

  int number_of_integrals_per_thread;

  int index_integrands_first;
  int index_integrands_last;








  //double  pk;

  FileName root; /**< root for all file names */
  FileName path_to_class; /**< root for all file names */
  FileName append_name_cobaya_ref;
  FileName path_to_ref_trispectrum_for_cobaya;
  FileName full_path_to_noise_curve_for_y_y;
  FileName full_path_to_dndz_gal;

 /* vector of all SZ quantities function of redshift*/

  int  tsz_size;

  int  index_flag_cov_N_cl;
  int  index_Rho_crit;
  int  index_Delta_c;
  int  index_rVIR;
  int  index_cVIR;
  int  index_c200m;
  int  index_r200m;
  int  index_mVIR;
  int  index_m500;
  int  index_r500;
  int  index_l500;
  int  index_ls;
  int  index_rs;
  int  index_m200;
  int  index_m180m;
  int  index_m200m;
  int  index_m1600m;
  int  index_m500c;
  int  index_mass_for_hmf;
  int  index_r500c;
  int  index_Rh;
  int  index_mf;
  int  index_dlognudlogRh;
  int  index_lognu;
  int  index_dlogSigma2dlogRh;
  int  index_dndlogRh;
  int  index_logSigma2;
  int  index_z;
  int  index_c200c;
  int  index_m200c;
  int  index_l200c;
  int  index_characteristic_multipole_for_nfw_profile;
  int  index_r200c;
  int  index_multipole;
  int  index_multipole_prime;
  int  index_mass_bin_1;
  int  index_mass_bin_2;
  int  index_multipole_1;
  int  index_multipole_2;
  int  index_multipole_3;
  int  index_redshift_for_dndlnM;
  int  index_mass_for_dndlnM;
  int  index_multipole_for_pressure_profile;
  int  index_pressure_profile;
  int  index_multipole_for_tau_profile;
  int  index_multipole_for_nfw_profile;
  int  index_tau_profile;
  int  index_lensing_profile;
  int  index_multipole_for_lensing_profile;
  int  index_completeness;
  int  index_te_of_m;
  int  index_volume;
  int  index_chi2; // in [Mpc/h]^2
  int  index_dgdz; // d(D/a)/dz = D(1-f)
  int  index_lensing_Sigma_crit;
  int  index_vrms2;
  int  index_pk_for_halo_bias;
  int  index_dlnMdeltadlnM;
  int  index_part_id_cov_hsv;

  int  index_mean_y;
  int  index_hmf;

  int index_sigma2_hsv;

  int  index_halo_bias;
  int  index_halo_bias_b2;
  int  index_k_value_for_halo_bias;

  int index_phi_galaxy_counts;
  int index_mean_galaxy_number_density;
  int index_c500c_KA20;
  int index_multipole_for_galaxy_profile;
  int index_galaxy_profile;

  int index_multipole_for_cib_profile;
  int index_frequency_for_cib_profile;
  int index_frequency_prime_for_cib_profile;
  int index_cib_profile;

  int index_W_lensmag;

  int index_k_for_pk_hm;
  int index_density_profile;

  int index_multipole_for_pk;

  //////////////

  int index_integral;
  int index_integral_te_y_y;
  int index_integral_2halo_term;

  int index_integral_trispectrum_first;
  int index_integral_trispectrum_last;

  int index_integral_cov_N_cl_first;
  int index_integral_cov_N_cl_last;

  int index_integral_N_for_cov_N_cl_first;
  int index_integral_N_for_cov_N_cl_last;


  int  index_integrals_over_m_first;
  int  index_integrals_over_m_last;

  int  index_integrals_over_z_first;
  int  index_integrals_over_z_last;



  int  index_integral_over_m;
  int  index_integral_te_y_y_over_m;
  int  index_integral_2halo_term_over_m;
  int  index_integral_trispectrum_first_over_m;
  int  index_integral_trispectrum_last_over_m;
  int  index_integral_cov_N_cl_first_over_m;
  int  index_integral_cov_N_cl_last_over_m;
  int  index_integral_N_for_cov_N_cl_first_over_m;
  int  index_integral_N_for_cov_N_cl_last_over_m;




  //mass bins for covariance between cluster counts and power spectrum
  int nbins_M;
  double * M_bins;
  double dlogM;
  double * cov_Y_N_mass_bin_edges;



  //HOD
  double M_min_HOD;
  double sigma_lnM_HOD;
  double alpha_s_HOD;
  double M1_prime_HOD;
  double rho_y_gal;

  double M_min_HOD_mass_factor_unwise;
  double x_out_truncated_nfw_profile;
  double x_out_nfw_profile;
  double M_min_HOD_satellite_mass_factor_unwise;
  double M1_prime_HOD_factor;
  double cvir_tau_profile_factor;

  int hm_consistency;


  // noise curve for cov(y,y)

  int include_noise_cov_y_y;

  //units for tSZ spectrum
  double exponent_unit;

  //completeness
  double theta_bin_min;
  double theta_bin_max;
  int nthetas;
  double * thetas;

  double *skyfracs;
  int nskyfracs;


  double ** ylims;
  double * sky_averaged_ylims;


  int experiment;
  //SO completeness
  double * SO_thetas;
  double * SO_Qfit;
  int  SO_Q_size;

  double * SO_RMS;
  double * SO_skyfrac;
  int  SO_RMS_size;

  //INPUT PARAMETERS
  int nlSZ;
  int n_ell_independent_integrals;

  double * l_unwise_filter;
  double * f_unwise_filter;
  int unwise_filter_size;




  /*Redshift limits for the integration*/
  double z1SZ;
  double z2SZ;

  double z1SZ_dndlnM;
  double z2SZ_dndlnM;

  double M1SZ_dndlnM;
  double M2SZ_dndlnM;


  double z1SZ_L_sat;
  double z2SZ_L_sat;

  double M1SZ_L_sat;
  double M2SZ_L_sat;

  double epsabs_L_sat;
  double epsrel_L_sat;


  int n_z_W_lensmag;

  /*Array size*/
  int n_arraySZ;//number of z in the interpolation
  int n_arraySZ_for_integral;//number of z in the integration

  int n_z_dndlnM;
  int n_m_dndlnM;

  int n_z_L_sat;
  int n_m_L_sat;

  int N_redshift_dndlnM;
  int N_mass_dndlnM;

  //mass limits: h^-1 Msun
  double M1SZ;
  double M2SZ;

  double delta_alpha;
  double alpha_p;

  double alpha_b;
  double Ap;
  int mass_dependent_bias;

  //Planck pressure profile
  double P0GNFW;
  double c500;
  double gammaGNFW;
  double alphaGNFW;
  double betaGNFW;

  double ln_x_size_for_pp;
  double * ln_x_for_pp;

  double x_size_for_pp;
  double * x_for_pp;


  //Battaglia pressure profile
  double P0_B12;
  double xc_B12;
  double beta_B12;

  double alpha_m_P0_B12;
  double alpha_m_xc_B12;
  double alpha_m_beta_B12;

  double alpha_z_P0_B12;
  double alpha_z_xc_B12;
  double alpha_z_beta_B12;

// JCH
//double precision :: f_free=0.85d0 !for kSZ calculations, fraction of free electrons w.r.t. total
//double precision :: mu_e=1.14d0 !mean molecular weight per electron, for primordial composition

  double f_free;
  double mu_e;

  /*Pressure profile is considered between x_in and x_out*/
  double x_inSZ;
  double x_outSZ;

  double HSEbias;

  /*For the computation of sigma2*/
  int  ndimSZ;
  double logR1SZ; // 0.0034Mpc/h, 1.8e4  solar mass
  double logR2SZ; // 54.9Mpc/h, 7.5e16 solar mass
  double delta_cSZ;



  /*Multplicity function Tinker 2010*/

  double alphaSZ;
  double beta0SZ;
  double gamma0SZ;

  double phi0SZ;
  double eta0SZ;


  /*Multplicity function Bocquet 2015*/

  double Ap0;
  double a0;
  double b0;
  double c0;

  int pk_nonlinear_for_vrms2;

  int MF;
  //1:Tinker 2010 (T10)
  //2:Bocquet 2015 (B15)
  //3:Jenkins 2001 (J01)
  //4:Tinker 2008 (T08)
  //5:Tinker 2008 interpolated @ M500 (T08@M500)

  //Precision Parameters For qromb_sz_integrand
  int K;
  double EPS;
  double JMAX;


  //Precision Parameters For qromb_sz_sigma
  int K_sigma;
  double EPS_sigma;
  double JMAX_sigma;

  ////////////////////////
  //integration method and parameters (mass)
  int integration_method_mass;

  double redshift_epsrel;
  double redshift_epsabs;

  double mass_epsrel;
  double mass_epsabs;

  double pressure_profile_epsabs;
  double pressure_profile_epsrel;
  double nu_y_dist_GHz;

  int cib_frequency_list_num;
  int cib_dim;
  double * cib_frequency_list;

  int id_nu_cib_to_save;
  int id_nu_prime_cib_to_save;

  // Table 1  of MM20
  double alpha_cib; //redshift evolution of dust temperature
  double T0_cib; // dust temperature today
  double beta_cib; // emissivity index of sed
  double gamma_cib; // Power law index of SED at high frequency
  double delta_cib; // Redshift evolution of L − M normalisation
  double m_eff_cib; // Most efficient halo mass in Msun/h
  double L0_cib; // Normalisation of L − M relation
  double sigma2_LM_cib; // Size of of halo masses sourcing CIB emission

  double nfw_profile_epsabs;
  double nfw_profile_epsrel;

  int patterson_show_neval;

  int number_of_mass_bins; //for trapezoidal rule
  ////////////////////////

  ////////////////////////
  //integration method and parameters (pressure profile)
  int integration_method_pressure_profile;

  //Foreground parameters
  double A_cib, A_rs, A_ir, A_cn;

  double * k_for_pk_hm;
  double dlnk_for_pk_hm;
  double k_min_for_pk_hm;
  double k_max_for_pk_hm;
  int n_k_for_pk_hm;
  double z_for_pk_hm;

  //Cl spectrum
  double * ell;
  double * ell_plc;
  double * ell_plc_no_low_ell;
  double * ell_plc_low;
  double * ell_mock;
  double * ell_trispectrum;
  double * x_gauss;
  double * w_gauss;

  double * ell_kSZ2_gal_multipole_grid;
  int N_kSZ2_gal_multipole_grid;



  double dlogell;
  double ell_min_mock;
  double ell_max_mock;




  double Tcmb_gNU_at_150GHz;
  double Tcmb_gNU;

  double Rho_crit_0;
  double D_0;
  double D_z1SZ;
  double Omega_m_0;
  double Omega_ncdm_0;

  double Sigma8OmegaM_SZ;
  double sigma8_Pcb;

  short has_vrms2;
  short has_sigma2_hsv;

  short has_tszspectrum;  //do we need tSZ spectrum? */
  short sz_verbose; /**< flag regulating the amount of information sent to standard output (none if set to zero) */
  short write_sz;  //do we need SZ quatitiies vs redshift? */

  short has_completeness_for_ps_SZ;
  short which_ps_sz;
  double H0_in_class_units;
  int ell_sz;
  // Figure 7 of KS02 -> KS02
  // Planck 2015 effective multipoles -> P15
  // SZFASTDKS -> DKS

  // halo occupation distribution
  int hod_model;


  int concentration_parameter;
  //Duffy 2008: D08
  //Seljak 2000: S00

  int pressure_profile;
  //Planck 2013 (P13)
  //Arnaud et al 2010 (A10)
  //Custom. GNFW

  int tau_profile;
  int tau_profile_mode;

  int HMF_prescription_NCDM;
  int effective_temperature;
  int temperature_mass_relation;
  int mean_y;

  double * PP_lnx;
  double * PP_lnI;
  double * PP_d2lnI;

  int PP_lnx_size;

  double * RNFW_lnx;
  double * RNFW_lnI;

  int RNFW_lnx_size;


  double * T10_ln1pz;
  double * T10_lnalpha;
  int T10_lnalpha_size;


  double * normalized_dndz_z;
  double * normalized_dndz_phig;

  int normalized_dndz_size;

  double * normalized_fdndz_z;
  double * normalized_fdndz_phig;

  int normalized_fdndz_size;

  double * normalized_cosmos_dndz_z;
  double * normalized_cosmos_dndz_phig;

  int normalized_cosmos_dndz_size;

  double * unbinned_nl_yy_ell;
  double * unbinned_nl_yy_n_ell;
  int nl_yy_is_binned;
  int unbinned_nl_yy_size;




  double * CM_redshift;
  double * CM_logM;

  int CM_redshift_size;
  int CM_logM_size;
  double * CM_logC;


  double ** array_profile_ln_rho_at_lnl_lnM_z;
  double * array_profile_ln_l;
  double * array_profile_ln_m;
  double * array_profile_ln_1pz;

  // int array_profile_ln_PgNFW_at_lnl_over_ls_size; defined in class_sz_precisions.h
  double * array_profile_ln_l_over_ls;
  double * array_profile_ln_PgNFW_at_lnl_over_ls;

  double * dndlnM_array_z;
  double * dndlnM_array_m;

  double * array_m_dndlnM;
  double * array_z_dndlnM;
  double * array_dndlnM_at_z_and_M;

  double * array_m_L_sat;
  double * array_z_L_sat;
  double ** array_L_sat_at_z_and_M_at_nu;
  //double * array_L_sat_at_z_and_M_at_nu_prime;

  double * array_z_W_lensmag;
  double * array_W_lensmag;

  double * array_redshift;
  double * array_radius;
  double * array_sigma_at_z_and_R;
  double * array_dsigma2dR_at_z_and_R;

  double * array_vrms2_at_z;
  double * array_sigma2_hsv_at_z;

  double * array_mean_galaxy_number_density;

  // int n_z_hmf_counter_terms;
  int hm_consistency_counter_terms_done;
  double * array_redshift_hmf_counter_terms;
  double * array_hmf_counter_terms_nmin;
  double * array_hmf_counter_terms_b1min;
  double * array_hmf_counter_terms_b2min;
  ErrorMsg error_message; /**< zone for writing error messages */


};

/*
 * Boilerplate for C++
 */
#ifdef __cplusplus
extern "C" {
#endif

int szpowerspectrum_init(struct background * pba,
                         struct thermo * pth,
                         struct nonlinear * pnl,
                         struct primordial * ppm,
                         struct tszspectrum * ptsz,
                         struct precision * ppr);


  int szpowerspectrum_free(struct tszspectrum *ptsz);


  int compute_sz(struct background * pba,
                 struct nonlinear * pnl,
                 struct primordial * ppm,
                 struct tszspectrum * ptsz,
                 double * pvecback,
                 double * Pvectsz);



  //This evaluates the integrand which will be integrated
  //over M and then over z
  double integrand_at_m_and_z(double logM ,
                              double * pvecback,
                              double * pvectsz,
                              struct background * pba,
                              struct primordial * ppm,
                              struct nonlinear * pnl,
                              struct tszspectrum * ptsz);

  double delta_ell_lens_at_ell_and_z( double * pvecback,
                                  double * pvectsz,
                                  struct background * pba,
                                  struct primordial * ppm,
                                  struct nonlinear * pnl,
                                  struct tszspectrum * ptsz);

  double delta_ell_isw_at_ell_and_z( double * pvecback,
                                  double * pvectsz,
                                  struct background * pba,
                                  struct primordial * ppm,
                                  struct nonlinear * pnl,
                                  struct tszspectrum * ptsz);

  int evaluate_HMF(double logM ,
                   double * pvecback,
                   double * pvectsz,
                   struct background * pba,
                   struct nonlinear * pnl,
                   struct tszspectrum * ptsz);

  int evaluate_completeness(double * pvecback,
                            double * pvectsz,
                            struct background * pba,
                            struct tszspectrum * ptsz);

  int evaluate_pressure_profile(double * pvecback,
                                double * pvectsz,
                                struct background * pba,
                                struct tszspectrum * ptsz);

  int evaluate_tau_profile(double * pvecback,
                           double * pvectsz,
                           struct background * pba,
                           struct tszspectrum * ptsz);

  int evaluate_lensing_profile(double * pvecback,
                               double * pvectsz,
                               struct background * pba,
                               struct tszspectrum * ptsz);



  int write_output_to_files_ell_indep_ints(struct nonlinear * pnl,
                                           struct background * pba,
                                           struct tszspectrum * ptsz);

  int write_output_to_files_cl(struct nonlinear * pnl,
                               struct background * pba,
                               struct tszspectrum * ptsz);


  int show_preamble_messages(struct background * pba,
                             struct thermo * pth,
                             struct nonlinear * pnl,
                             struct primordial * ppm,
                             struct tszspectrum * ptsz);

  int show_results(struct background * pba,
                   struct nonlinear * pnl,
                   struct primordial * ppm,
                   struct tszspectrum * ptsz);

  int select_multipole_array(struct tszspectrum * ptsz);

  int evaluate_halo_bias(double * pvecback,
                         double * pvectsz,
                         struct background * pba,
                         struct primordial * ppm,
                         struct nonlinear * pnl,
                         struct tszspectrum * ptsz);

  int evaluate_halo_bias_b2(double * pvecback,
                            double * pvectsz,
                            struct background * pba,
                            struct primordial * ppm,
                            struct nonlinear * pnl,
                            struct tszspectrum * ptsz);

 int evaluate_effective_galaxy_bias(double * pvecback,
                                    double * pvectsz,
                                    struct background * pba,
                                    struct primordial * ppm,
                                    struct nonlinear * pnl,
                                    struct tszspectrum * ptsz);


 int evaluate_pk_at_ell_plus_one_half_over_chi(double * pvecback,
                                              double * pvectsz,
                                              struct background * pba,
                                              struct primordial * ppm,
                                              struct nonlinear * pnl,
                                              struct tszspectrum * ptsz);

 int evaluate_pk_at_ell_plus_one_half_over_chi_today(double * pvecback,
                                                      double * pvectsz,
                                                      struct background * pba,
                                                      struct primordial * ppm,
                                                      struct nonlinear * pnl,
                                                      struct tszspectrum * ptsz);


double evaluate_pk_halofit_over_pk_linear_at_ell_plus_one_half_over_chi(double * pvecback,
                                                                     double * pvectsz,
                                                                     struct background * pba,
                                                                     struct primordial * ppm,
                                                                     struct nonlinear * pnl,
                                                                     struct tszspectrum * ptsz);

  int initialise_and_allocate_memory(struct tszspectrum * ptsz);


  int evaluate_temperature_mass_relation(double * pvecback,
                                         double * pvectsz,
                                         struct background * pba,
                                         struct tszspectrum * ptsz);

double evaluate_dlnMdeltadlnM(double logM,
                             double * pvecback,
                             double * pvectsz,
                             struct background * pba,
                             struct nonlinear * pnl,
                             struct tszspectrum * ptsz);

int evaluate_vrms2(double * pvecback,
                   double * pvectsz,
                   struct background * pba,
                   struct nonlinear * pnl,
                   struct tszspectrum * ptsz);


int evaluate_sigma2_hsv(double * pvecback,
                         double * pvectsz,
                         struct background * pba,
                         struct nonlinear * pnl,
                         struct tszspectrum * ptsz);

double integrand_patterson_test(double xi, void *p);


int write_redshift_dependent_quantities(struct background * pba,
                                        struct tszspectrum * ptsz);


int evaluate_tau_profile(double * pvecback,
                        double * pvectsz,
                        struct background * pba,
                        struct tszspectrum * ptsz);

int tabulate_density_profile(struct background * pba,
                             struct tszspectrum * ptsz);

int tabulate_pressure_profile_gNFW(struct background * pba,
                                   struct tszspectrum * ptsz);

int evaluate_mean_galaxy_number_density_at_z(double * pvectsz,
                                             struct tszspectrum * ptsz);

double HOD_mean_number_of_central_galaxies(double z,
                                           double M_halo,
                                           double M_min,
                                           double sigma_lnM,
                                           double * pvectsz,
                                           struct tszspectrum * ptsz,
                                           struct background * pba);

double HOD_mean_number_of_satellite_galaxies(double z,
                                             double M_halo,
                                             double Nc_mean,
                                             double M_min,
                                             double alpha_s,
                                             double M1_prime,
                                             struct tszspectrum * ptsz,
                                             struct background * pba);

int evaluate_galaxy_profile(double * pvecback,
                            double * pvectsz,
                            struct background * pba,
                            struct tszspectrum * ptsz);

double evaluate_truncated_nfw_profile(
                                   double * pvectsz,
                                   struct background * pba,
                                   struct tszspectrum * ptsz,
                                   int flag_matter_type);



int evaluate_c200m_D08(double * pvecback,
                        double * pvectsz,
                        struct background * pba,
                        struct tszspectrum * ptsz);

int evaluate_c200c_D08(double * pvecback,
                        double * pvectsz,
                        struct background * pba,
                        struct tszspectrum * ptsz);


int evaluate_c500c_KA20(//double * pvecback,
                        double * pvectsz,
                        struct background * pba,
                        struct tszspectrum * ptsz);


double radial_kernel_W_galaxy_at_z( double * pvecback,
                                    double * pvectsz,
                                    struct background * pba,
                                    struct tszspectrum * ptsz);

double radial_kernel_W_lensing_at_z(double * pvecback,
                                    double * pvectsz,
                                    struct background * pba,
                                    struct primordial * ppm,
                                    struct nonlinear * pnl,
                                    struct tszspectrum * ptsz);

double radial_kernel_W_lensing_magnification_at_z(double * pvecback,
                                                  double * pvectsz,
                                                  struct background * pba,
                                                  struct primordial * ppm,
                                                  struct nonlinear * pnl,
                                                  struct tszspectrum * ptsz);

double evaluate_galaxy_number_counts( double * pvecback,
                                    double * pvectsz,
                                    struct background * pba,
                                    struct tszspectrum * ptsz);

double evaluate_galaxy_number_counts_fdndz( double * pvecback,
                                    double * pvectsz,
                                    struct background * pba,
                                    struct tszspectrum * ptsz);
double evaluate_unwise_m_min_cut(double z,
                                 int sample_id,
                                 struct tszspectrum * ptsz);


int evaluate_cib_profile(double * pvecback,
                         double * pvectsz,
                         struct background * pba,
                         struct tszspectrum * ptsz);

double Luminosity_of_central_galaxies(double z,
                                      double  M_halo,
                                      double nu,
                                      double * pvectsz,
                                      struct tszspectrum * ptsz,
                                      struct background * pba);

double Luminosity_of_satellite_galaxies(double z,
                                        double  M_halo,
                                        double nu,
                                        struct tszspectrum * ptsz,
                                        struct background * pba);

double evaluate_Sigma_cib(double M, struct tszspectrum * ptsz);
double evaluate_phi_cib(double z, struct tszspectrum * ptsz);
double evaluate_sed_cib(double z, double nu, struct tszspectrum * ptsz);
double evaluate_dust_temperature(double z, struct tszspectrum * ptsz);
double evaluate_galaxy_luminosity(double z, double M, double nu, struct tszspectrum * ptsz);
double subhalo_hmf_dndlnMs(double M_host,double M_sub);

double integrand_kSZ2_X_at_theta(double ell_prime, void *p);

int evaluate_density_profile(double * pvecback,
                             double * pvectsz,
                             struct background * pba,
                             struct tszspectrum * ptsz);

double bispectrum_f2_kernel(double k,
                            double k_prime,
                            double k_prime_prime);


double get_second_order_bias_at_z_and_nu(double z,
                                     double nu,
                                     struct tszspectrum * ptsz);

double get_first_order_bias_at_z_and_nu(double z,
                                         double nu,
                                         struct tszspectrum * ptsz);


double get_sigma_at_z_and_m(double z,
                            double m,
                            struct tszspectrum * ptsz,
                            struct background * pba);

double get_nu_at_z_and_m(double z,
                         double m,
                         struct tszspectrum * ptsz,
                         struct background * pba);

struct Parameters_for_integrand_kSZ2_X_at_theta{
  struct tszspectrum * ptsz;
  double theta;
  int index_ell_3;
  double * b_l1_l2_l_1d;
  double * ln_ell;
};







#ifdef __cplusplus
}
#endif

#endif
