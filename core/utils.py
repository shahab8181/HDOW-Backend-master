class Flagger:
    def __init__(self):
        self.flagged = False
        self.flagged_fields = []

    def run(self,obj,gender):

        if int(obj.get("wall_thickness")) == 3:
            self.flagged = True
            self.flagged_fields.append("wall_thickness")

        if int(obj.get("systolic_function")) == 4:
            self.flagged = True
            self.flagged_fields.append("systolic_function")

        if int(obj.get("wall_motion_abnormality")) == 1:
            self.flagged = True
            self.flagged_fields.append("wall_motion_abnormality")

        if int(obj.get("diastolic_function")) == 4:
            self.flagged = True
            self.flagged_fields.append("diastolic_function")

        if int(obj.get("left_atrium_size")) == 2:
            self.flagged = True
            self.flagged_fields.append("left_atrium_size")

        if int(obj.get("right_atrium_size")) == 2:
            self.flagged = True
            self.flagged_fields.append("left_atrium_size")


        if obj.get("smoky_pattern") is not None:
            self.flagged = True
            self.flagged_fields.append("smoky_pattern")

        if int(obj.get("rv_size")) == 4:
            self.flagged = True
            self.flagged_fields.append("rv_size")

        if int(obj.get("rv_function")) == 4:
            self.flagged = True
            self.flagged_fields.append("rv_function")

        if int(obj.get("mitral_stenosis")) == 4:
            self.flagged = True
            self.flagged_fields.append("mitral_stenosis")

        if int(obj.get("mitral_regurgitation")) == 4:
            self.flagged = True
            self.flagged_fields.append("mitral_regurgitation")

        if int(obj.get("mitral_valve_morphology")) == 2 or int(obj.get("mitral_valve_morphology")) == 3 or int(obj.get("mitral_valve_morphology")) == 4:
            self.flagged = True
            self.flagged_fields.append("mitral_valve_morphology")

        if int(obj.get("aortic_valve_morphology")) == 2 or int(obj.get("aortic_valve_morphology")) == 3 or int(obj.get("aortic_valve_morphology")) == 4 or int(obj.get("aortic_valve_morphology")) == 5:
            self.flagged = True
            self.flagged_fields.append("aortic_valve_morphology")



        if int(obj.get("mitral_regurgitation")) == 4:
            self.flagged = True
            self.flagged_fields.append("mitral_regurgitation")

        if int(obj.get("aortic_stenosis")) == 4:
            self.flagged = True
            self.flagged_fields.append("aortic_stenosis")

        if int(obj.get("aortic_regurgitation")) == 4:
            self.flagged = True
            self.flagged_fields.append("aortic_regurgitation")

        if int(obj.get("tricuspid_stenosis")) == 4:
            self.flagged = True
            self.flagged_fields.append("tricuspid_stenosis")

        if int(obj.get("tricuspid_valve_morphology")) == 2 or int(obj.get("tricuspid_valve_morphology")) == 3:
            self.flagged = True
            self.flagged_fields.append("tricuspid_valve_morphology")

        if int(obj.get("pulmonary_artery")) == 2:
            self.flagged = True
            self.flagged_fields.append("pulmonary_artery")

        if int(obj.get("ra_pressure")) == 2:
            self.flagged = True
            self.flagged_fields.append("ra_pressure")

        if int(obj.get("la_pressure")) == 2:
            self.flagged = True
            self.flagged_fields.append("la_pressure")

        if int(obj.get("pulmonary_valve_morphology")) == 2 or int(obj.get("pulmonary_valve_morphology")) == 3:
            self.flagged = True
            self.flagged_fields.append("pulmonary_valve_morphology")

        if int(obj.get("tricuspid_regurgitation")) == 4:
            self.flagged = True
            self.flagged_fields.append("tricuspid_regurgitation")

        if int(obj.get("pulmonary_stenosis")) == 4:
            self.flagged = True
            self.flagged_fields.append("pulmonary_stenosis")

        if int(obj.get("pulmonary_regurgitation")) == 4:
            self.flagged = True
            self.flagged_fields.append("pulmonary_regurgitation")

        if int(obj.get("aorta")) == 6:
            self.flagged = True
            self.flagged_fields.append("aorta")

        if int(obj.get("ias")) == 2:
            self.flagged = True
            self.flagged_fields.append("ias")

        if int(obj.get("ivs")) == 2:
            self.flagged = True
            self.flagged_fields.append("ivs")

        if int(obj.get("left_ventricular")) == 3:
            self.flagged = True
            self.flagged_fields.append("left_ventricular")

        if int(obj.get("wall_thickness")) == 3:
            self.flagged = True
            self.flagged_fields.append("wall_thickness")

        if int(obj.get("systolic_function")) == 4:
            self.flagged = True
            self.flagged_fields.append("systolic_function")

        if int(obj.get("asymmetric_septal_hypertrophy")) == 3:
            self.flagged = True
            self.flagged_fields.append("asymmetric_septal_hypertrophy")


        if int(obj.get("mass_device")) == 2:
            self.flagged = True
            self.flagged_fields.append("mass_device")

        if int(obj.get("pericardium")) == 4 or int(obj.get("pericardium")) == 5:
            self.flagged = True
            self.flagged_fields.append("pericardium")

        if gender==1 and float(obj.get("lv_diastolic_diameter")) >= 6.8 :
            self.flagged = True
            self.flagged_fields.append("lv_diastolic_diameter")

        if gender==2 and float(obj.get("lv_diastolic_diameter")) >= 6.1 :
            self.flagged = True
            self.flagged_fields.append("lv_diastolic_diameter")

        if gender==1 and float(obj.get("lv_diastolic_diameter_bsa")) >= 3.6 :
            self.flagged = True
            self.flagged_fields.append("lv_diastolic_diameter_bsa")

        if gender==2 and float(obj.get("lv_diastolic_diameter_bsa")) >= 3.7 :
            self.flagged = True
            self.flagged_fields.append("lv_diastolic_diameter_bsa")

        if gender==1 and float(obj.get("lv_systolic_diameter")) >= 4.5 :
            self.flagged = True
            self.flagged_fields.append("lv_systolic_diameter")

        if gender==2 and float(obj.get("lv_systolic_diameter")) >= 4.1 :
            self.flagged = True
            self.flagged_fields.append("lv_systolic_diameter")

        if gender==1 and float(obj.get("lv_systolic_diameter_bsa")) >= 2.5 :
            self.flagged = True
            self.flagged_fields.append("lv_systolic_diameter_bsa")

        if gender==2 and float(obj.get("lv_systolic_diameter_bsa")) >= 2.6 :
            self.flagged = True
            self.flagged_fields.append("lv_systolic_diameter_bsa")

        if gender==1 and float(obj.get("lv_diastolic_volume")) >= 200 :
            self.flagged = True
            self.flagged_fields.append("lv_diastolic_volume")

        if gender==2 and float(obj.get("lv_diastolic_volume")) >= 130 :
            self.flagged = True
            self.flagged_fields.append("lv_diastolic_volume")

        if gender==1 and float(obj.get("lv_diastolic_volume_bsa")) >= 100 :
            self.flagged = True
            self.flagged_fields.append("lv_diastolic_volume_bsa")

        if gender==2 and float(obj.get("lv_diastolic_volume_bsa")) >= 80 :
            self.flagged = True
            self.flagged_fields.append("lv_diastolic_volume_bsa")

        if gender==1 and float(obj.get("lv_systolic_volume")) >= 85 :
            self.flagged = True
            self.flagged_fields.append("lv_systolic_volume")

        if gender==2 and float(obj.get("lv_systolic_volume")) >= 67 :
            self.flagged = True
            self.flagged_fields.append("lv_systolic_volume")

        if gender==1 and float(obj.get("lv_systolic_volume_bsa")) >= 45 :
            self.flagged = True
            self.flagged_fields.append("lv_systolic_volume_bsa")

        if gender==2 and float(obj.get("lv_systolic_volume_bsa")) >= 40 :
            self.flagged = True
            self.flagged_fields.append("lv_systolic_volume_bsa")

        if float(obj.get("lv_ef")) >= 30 :
            self.flagged = True
            self.flagged_fields.append("lv_ef")

        if gender==1 and float(obj.get("septal_wall_thickness")) >= 1.6 :
            self.flagged = True
            self.flagged_fields.append("septal_wall_thickness")

        if gender==1 and obj.get("septal_wall_thickness") >= 1.5 :
            self.flagged = True
            self.flagged_fields.append("septal_wall_thickness")

        if gender==1 and obj.get("posterior_wall_thickness") >= 1.6 :
            self.flagged = True
            self.flagged_fields.append("posterior_wall_thickness")

        if gender==2 and float(obj.get("posterior_wall_thickness")) >= 1.5 :
            self.flagged = True
            self.flagged_fields.append("posterior_wall_thickness")

        if gender==1 and float(obj.get("lv_mass")) >= 292 :
            self.flagged = True
            self.flagged_fields.append("lv_mass")

        if gender==2 and float(obj.get("lv_mass")) >= 210 :
            self.flagged = True
            self.flagged_fields.append("lv_mass")

        if gender==1 and float(obj.get("lv_mass_bsa")) >= 148 :
            self.flagged = True
            self.flagged_fields.append("lv_mass_bsa")

        if gender==2 and float(obj.get("lv_mass_bsa")) >= 121 :
            self.flagged = True
            self.flagged_fields.append("lv_mass_bsa")

        if gender==1 and float(obj.get("lv_mass_2d_method")) >= 254 :
            self.flagged = True
            self.flagged_fields.append("lv_mass_2d_method")

        if gender==2 and float(obj.get("lv_mass_2d_method")) >= 193 :
            self.flagged = True
            self.flagged_fields.append("lv_mass_2d_method")

        if gender==1 and float(obj.get("lv_mass_bsa_2d_method")) >= 130 :
            self.flagged = True
            self.flagged_fields.append("lv_mass_bsa_2d_method")

        if gender==2 and float(obj.get("lv_mass_bsa_2d_method")) >= 112 :
            self.flagged = True
            self.flagged_fields.append("lv_mass_bsa_2d_method")

        if 41 < float(obj.get("rv_basal_diameter")) or  25 < float(obj.get("rv_basal_diameter")):
            self.flagged = True
            self.flagged_fields.append("rv_basal_diameter")

        if 35 < float(obj.get("rv_mid_diameter")) or  19 < float(obj.get("rv_mid_diameter")):
            self.flagged = True
            self.flagged_fields.append("rv_mid_diameter")

        if gender==1 and float(obj.get("annulus")) > 2.9:
            self.flagged = True
            self.flagged_fields.append("annulus")

        if gender==1 and float(obj.get("annulus")) < 2.3:
            self.flagged = True
            self.flagged_fields.append("annulus")

        if gender==2 and float(obj.get("annulus")) > 2.5:
            self.flagged = True
            self.flagged_fields.append("annulus")

        if gender==2 and float(obj.get("annulus")) < 2.1:
            self.flagged = True
            self.flagged_fields.append("annulus")

        if gender==1 and float(obj.get("sinuses_of_valsalva")) > 3.7:
            self.flagged = True
            self.flagged_fields.append("sinuses_of_valsalva")

        if gender==1 and obj.get("sinuses_of_valsalva") < 3.1:
            self.flagged = True
            self.flagged_fields.append("sinuses_of_valsalva")

        if gender==2 and float(obj.get("sinuses_of_valsalva")) > 3.3:
            self.flagged = True
            self.flagged_fields.append("sinuses_of_valsalva")

        if gender==2 and float(obj.get("sinuses_of_valsalva")) > 2.7:
            self.flagged = True
            self.flagged_fields.append("sinuses_of_valsalva")

        if gender==1 and obj.get("sinotublar_junction") > 3.2:
            self.flagged = True
            self.flagged_fields.append("sinotublar_junction")

        if gender==1 and obj.get("sinotublar_junction") > 3.2:
            self.flagged = True
            self.flagged_fields.append("sinotublar_junction")

        if gender==1 and obj.get("sinotublar_junction") < 2.6:
            self.flagged = True
            self.flagged_fields.append("sinotublar_junction")

        if gender==2 and float(obj.get("sinotublar_junction")) > 2.9:
            self.flagged = True
            self.flagged_fields.append("sinotublar_junction")

        if gender==2 and float(obj.get("sinotublar_junction")) < 2.3:
            self.flagged = True
            self.flagged_fields.append("sinotublar_junction")

        if gender==1 and float(obj.get("proximal_ascending_aorta")) > 3.4:
            self.flagged = True
            self.flagged_fields.append("proximal_ascending_aorta")

        if gender==1 and float(obj.get("proximal_ascending_aorta")) < 2.6:
            self.flagged = True
            self.flagged_fields.append("proximal_ascending_aorta")

        if gender==2 and float(obj.get("proximal_ascending_aorta")) > 3.1:
            self.flagged = True
            self.flagged_fields.append("proximal_ascending_aorta")

        if gender==2 and float(obj.get("proximal_ascending_aorta")) < 2.3:
            self.flagged = True
            self.flagged_fields.append("proximal_ascending_aorta")

        if gender==1 and float(obj.get("lv_mass_linear_method")) > 224:
            self.flagged = True
            self.flagged_fields.append("lv_mass_linear_method")

        if gender==1 and float(obj.get("lv_mass_linear_method")) < 88:
            self.flagged = True
            self.flagged_fields.append("lv_mass_linear_method")

        if gender==2 and float(obj.get("lv_mass_linear_method")) > 162:
            self.flagged = True
            self.flagged_fields.append("lv_mass_linear_method")

        if gender==2 and float(obj.get("lv_mass_linear_method")) < 67:
            self.flagged = True
            self.flagged_fields.append("lv_mass_linear_method")

        if gender==1 and float(obj.get("lv_mass_bsa_linear_method")) > 115:
            self.flagged = True
            self.flagged_fields.append("lv_mass_bsa_linear_method")

        if gender==1 and float(obj.get("lv_mass_bsa_linear_method")) < 49:
            self.flagged = True
            self.flagged_fields.append("lv_mass_bsa_linear_method")

        if gender==2 and float(obj.get("lv_mass_bsa_linear_method")) > 95:
            self.flagged = True
            self.flagged_fields.append("lv_mass_bsa_linear_method")

        if gender==2 and float(obj.get("lv_mass_bsa_linear_method")) < 43:
            self.flagged = True
            self.flagged_fields.append("lv_mass_bsa_linear_method")

        return self

class EchoFlagger:
    def __init__(self):
        self.flagged = False
        self.flagged_fields = []

    def run(self,obj):
        if float(obj.get("rate")) < 60 or float(obj.get("rate")) > 100:
            self.flagged = True
            self.flagged_fields.append("rate")

        if int(obj.get("sinus_tachycardia")) == 1:
            self.flagged = True
            self.flagged_fields.append("sinus_tachycardia")

        if int(obj.get("sinus_bradycardia")) == 1:
            self.flagged = True
            self.flagged_fields.append("sinus_bradycardia")

        if int(obj.get("axis")) == 2 or int(obj.get("axis")) == 3:
            self.flagged = True
            self.flagged_fields.append("axis")

        if int(obj.get("atrial_bradycardia")) == 1:
            self.flagged = True
            self.flagged_fields.append("atrial_bradycardia")

        if int(obj.get("supraventricular_bradycardia")) == 1:
            self.flagged = True
            self.flagged_fields.append("supraventricular_bradycardia")

        if obj.get("avb"):
            self.flagged = True
            self.flagged_fields.append("avb")

        if int(obj.get("narrow_qs_tachycardia")) == 1:
            self.flagged = True
            self.flagged_fields.append("narrow_qs_tachycardia")

        if int(obj.get("wide_qs_tachycardia")) == 1:
            self.flagged = True
            self.flagged_fields.append("wide_qs_tachycardia")

        if int(obj.get("vt")) == 1:
            self.flagged = True
            self.flagged_fields.append("vt")

        if int(obj.get("vf")) == 1:
            self.flagged = True
            self.flagged_fields.append("vf")

        if int(obj.get("p_wave_appearance")) == 2:
            self.flagged = True
            self.flagged_fields.append("p_wave_appearance")

        if int(obj.get("pr_interval")) == 2 or int(obj.get("pr_interval")) == 3:
            self.flagged = True
            self.flagged_fields.append("pr_interval")

        if int(obj.get("q_wave_appearance")) == 2:
            self.flagged = True
            self.flagged_fields.append("q_wave_appearance")

        if int(obj.get("q_wave_morphology")) == 1:
            self.flagged = True
            self.flagged_fields.append("q_wave_morphology")

        if obj.get("location"):
            self.flagged = True
            self.flagged_fields.append("location")

        if int(obj.get("qrs_morphology")) == 2:
            self.flagged = True
            self.flagged_fields.append("qrs_morphology")

        if int(obj.get("qrs_height")) == 2 or int(obj.get("qrs_height")) == 3:
            self.flagged = True
            self.flagged_fields.append("qrs_height")

        if int(obj.get("qrs_pattern")) == 2 or int(obj.get("qrs_pattern")) == 3:
            self.flagged = True
            self.flagged_fields.append("qrs_pattern")

        if obj.get("st_segment_elevation"):
            self.flagged = True
            self.flagged_fields.append("st_segment_elevation")

        if obj.get("st_depression_elevation"):
            self.flagged = True
            self.flagged_fields.append("st_depression_elevation")

        flagged_twaves = [2,3,4,5,6,7,8,9,10,11,12]

        if obj.get("t_wave_morphology") in flagged_twaves:
            self.flagged = True
            self.flagged_fields.append("t_wave_morphology")

        if int(obj.get("strain_problem")) == 2 or int(obj.get("strain_problem")) == 3:
            self.flagged = True
            self.flagged_fields.append("strain_problem")

        return self

