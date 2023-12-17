from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.postgres.fields import ArrayField
import math


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        male = ('male', 'male')
        female = ('female', 'female')

    ROLE_CHOICES = (
        (1, 'Technician'),
        (2, 'Supervisor'),
        (3, 'Patient'),
        (4, 'Doctor'),
    )

    age = models.IntegerField(blank=True, default=0, null=True)
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=100, choices=GenderChoices.choices, blank=True, null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True, upload_to='images')
    phone = models.CharField(max_length=20,blank=True,null=True)
    address = models.CharField(max_length=500,blank=True,null=True)
    create_at = models.DateField(auto_now=True)
    def __str__(self) -> str:
        return self.username
        # return self.first_name + ' ' + self.last_name


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.id


class MedicalDoctor(models.Model):
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )

    account = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=150, blank=True, null=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    @property
    def fullname(obj):
        return obj.account.first_name + obj.account.last_name

    def __str__(self):
        return str(self.account)




class Study(models.Model):


    STUDY_QUALITY_CHOICES = (
        (1, '2D'),
        (2, 'CW'),
        (3, 'PW'),
        (4, 'Color Doppler echocardiography'),
        (5,'M-Mode')
    )

    RECOMMENDATION_CHOICES = (
        (1, 'Emergent transport to the hospital'),
        (2, 'Emergency cardiologist consult'),
        (3, 'Cardiologist consult as soon as possible'),
        (4, 'Refer to GP')
    )
    client = models.OneToOneField('Case', on_delete=models.CASCADE, blank=True, null=True, related_name='study')
    study_quality = models.ManyToManyField('StudyQualityOptions', blank=True, null=True,related_name='StudyQualityOptions_set')

    # Physical Exam Fields
    height = models.DecimalField(decimal_places=1, max_digits=100, blank=True, null=True)
    weight = models.DecimalField(decimal_places=1, max_digits=100, blank=True, null=True)
    sbp = models.DecimalField(decimal_places=1, max_digits=100,blank=True,null=True)
    dbp = models.DecimalField(decimal_places=1, max_digits=100,blank=True,null=True)

    # Left Ventricular
    left_ventricular_choices = (
        (1, "Normal LV Cavity Size"),
        (2, "Mild Enlarged LV Cavity Size"),
        (3, "Severe Enlarged LV Cavity Size")
    )
    wall_thickness_choices = (
        (1, "Mild LVH"),
        (2, "Moderate LVH"),
        (3, "Severe LVH"),
        (4,"Normal")
    )
    asymmetric_septal_hypertrophy_choices = (
        (1, "Yes"),
        (2, "No"),
        (3,"Yes With LVOT Gradient"),
        (4,"Yes Without LVOT Gradient")
    )
    diastolic_function_choices = (
        (1, "Normal"),
        (2, "Mild Dysfunction"),
        (3, "Moderate Dysfunction"),
        (4, "Severe Dysfunction")
    )

    systolic_function_choices = (
        (1,"No"),
        (2,"Yes,Mild(40-49%)"),
        (3,"Yes,Moderate(30-39%)"),
        (4,"Yes,Severe(less than 30%)")
    )

    boolean_choices = (
        (1,"Yes"),
        (2,"No")
    )

    left_ventricular = models.PositiveSmallIntegerField(choices=left_ventricular_choices, blank=True, null=True)
    wall_thickness = models.PositiveSmallIntegerField(choices=wall_thickness_choices, blank=True, null=True)
    asymmetric_septal_hypertrophy = models.PositiveSmallIntegerField(choices=asymmetric_septal_hypertrophy_choices,
                                                                     blank=True, null=True)
    global_ef = models.DecimalField(decimal_places=1, max_digits=100,null=True,blank=True)
    ef_by_simpson_method = models.DecimalField(decimal_places=1, max_digits=100,blank=True, null=True)
    wall_motion_abnormality = models.PositiveSmallIntegerField(choices=boolean_choices,blank=True, null=True)
    diastolic_function = models.PositiveSmallIntegerField(choices=diastolic_function_choices, blank=True, null=True)
    systolic_function = models.PositiveBigIntegerField(choices=systolic_function_choices,blank=True, null=True)

    # Left Atrium
    left_atrium_size_choices = (
        (1, "Normal"),
        (2, "Enlarged")
    )
    la_pressure_choices = (
        (1, "Normal (<10mmHg)"),
        (2, "Increased")
    )
    left_atrium_size = models.PositiveSmallIntegerField(choices=left_atrium_size_choices, blank=True, null=True)
    la_pressure = models.PositiveSmallIntegerField(choices=la_pressure_choices, blank=True, null=True)

    smoky_pattern = models.PositiveSmallIntegerField(choices=boolean_choices,blank=True, null=True)

    # Left Atrium
    right_atrium_size_choices = (
        (1, "Normal Size"),
        (2, "Enlarged")
    )
    ra_pressure_choices = (
        (1, "Normal (<5mmHg)"),
        (2, "Increased")
    )
    right_atrium_size = models.PositiveSmallIntegerField(choices=right_atrium_size_choices, blank=True, null=True)
    ra_pressure = models.PositiveSmallIntegerField(choices=ra_pressure_choices, blank=True, null=True)

    # Right Ventricle
    rv_size_choices = (
        (1, "Normal"),
        (2, "Enlarged (Mild)"),
        (3, "Enlarged (Moderate)"),
        (4, "Enlarged (Severe)")
    )
    rv_function_choices = (
        (1, "Normal"),
        (2, "Decreased (Mild)"),
        (3, "Decreased (Moderate)"),
        (4, "Decreased (Severe)")
    )
    mitral_valve_morphology_choices = (
        (1, "Normal"),
        (2, "Rheumatismal"),
        (3, "Annular Calcification"),
        (4, "Prosthetic Valve")
    )
    mitral_stenosis_choices = (
        (1, "No"),
        (2, "Mild"),
        (3, "Moderate"),
        (4, "Severe")
    )

    mitral_regurgitation_choices = (
        (1, "No"),
        (2, "Mild"),
        (3, "Moderate"),
        (4, "Severe")
    )
    aortic_valve_morphology_choices = (
        (1, "Normal"),
        (2, "Bicuspid"),
        (3, "Rheumatismal"),
        (4, "Annular Calcification"),
        (5, "Prosthetic Valve")
    )
    aortic_stenosis_choices = (
        (1, "No"),
        (2, "Mild"),
        (3, "Moderate"),
        (4, "Severe")
    )
    aortic_regurgitation_choices = (
        (1, "No"),
        (2, "Mild"),
        (3, "Moderate"),
        (4, "Severe")
    )
    tricuspid_valve_morphology_choices = (
        (1, "Normal"),
        (2, "Abnormal"),
        (3, "Prosthetic Valve")
    )
    tricuspid_stenosis_choices = (
        (1, "No"),
        (2, "Mild"),
        (3, "Moderate"),
        (4, "Severe")
    )
    tricuspid_regurgitation_choices = (
        (1, "No"),
        (2, "Mild"),
        (3, "Moderate"),
        (4, "Severe")
    )
    pulmonary_valve_morphology_choices = (
        (1, "Normal"),
        (2, "Abnormal"),
        (3, "Prosthetic Valve")
    )
    pulmonary_stenosis_choices = (
        (1, "No"),
        (2, "Mild"),
        (3, "Moderate"),
        (4, "Severe")
    )
    pulmonary_regurgitation_choices = (
        (1, "No"),
        (2, "Mild"),
        (3, "Moderate"),
        (4, "Severe")
    )
    aorta_choices = (
        (1, "Left Side"),
        (2, "Right Side"),
        (3, "Dilatation"),
        (4, "Dissection")
    )
    pulmonary_artery_choices = (
        (1,"The main pulmonary artery and its proximal branches are confluent with normal size"),
        (2,"Abnormal")
    )
    ias_choices = (
        (1,"No evidence of interatrial communication by colour flow Doppler analysis"),
        (2,"ASD"),
        (3,"IA Aneurysm")
    )
    ivs_choices = (
        (1,"No evidence of interventricular communication by color flow Doppler analysis"),
        (2,"VSD")
    )
    mass_device_choices = (
        (1,"There is no visible mass or clot in cardiac chambers or great vessels"),
        (2,"Thrombosis"),
        (3,"Mass"),
        (4,"Device lead")
    )
    pericardium_choices = (
        (1,"Normal"),
        (2,"Effusion (Mild)"),
        (3, "Effusion (Moderate)"),
        (4,"Effusion (Severe)"),
        (5,"Effusion (Tamponade)"),
        (6,"Effusion (CP)")
    )

    FLAGGED_CHOICES = (
        (0,"False"),
        (1,"True")
    )

    rv_size = models.PositiveSmallIntegerField(choices=rv_size_choices, blank=True, null=True)
    rv_function = models.PositiveSmallIntegerField(choices=rv_function_choices, blank=True, null=True)
    mitral_valve_morphology = models.PositiveSmallIntegerField(choices=mitral_valve_morphology_choices, blank=True, null=True)
    mitral_stenosis = models.PositiveSmallIntegerField(choices=mitral_stenosis_choices, blank=True, null=True)
    mitral_regurgitation = models.PositiveSmallIntegerField(choices=mitral_regurgitation_choices, blank=True, null=True)

    # Aortic Valve
    aortic_valve_morphology = models.PositiveSmallIntegerField(choices=aortic_valve_morphology_choices, blank=True, null=True)
    aortic_stenosis = models.PositiveSmallIntegerField(choices=aortic_stenosis_choices, blank=True, null=True)
    aortic_regurgitation = models.PositiveSmallIntegerField(choices=aortic_regurgitation_choices, blank=True, null=True)

    # Tricuspid Valve
    tricuspid_valve_morphology = models.PositiveSmallIntegerField(choices=tricuspid_valve_morphology_choices,
                                                                  blank=True, null=True)
    tricuspid_stenosis = models.PositiveSmallIntegerField(choices=tricuspid_stenosis_choices, blank=True, null=True)
    tricuspid_regurgitation = models.PositiveSmallIntegerField(choices=tricuspid_regurgitation_choices, blank=True, null=True)
    trpg = models.IntegerField(blank=True, null=True)
    # Pulmonary Valve
    pulmonary_valve_morphology = models.PositiveSmallIntegerField(choices=pulmonary_valve_morphology_choices,
                                                                  blank=True, null=True)
    pulmonary_stenosis = models.PositiveSmallIntegerField(choices=pulmonary_stenosis_choices, blank=True, null=True)
    pg = models.IntegerField(blank=True, null=True)
    pulmonary_regurgitation = models.PositiveSmallIntegerField(choices=pulmonary_regurgitation_choices, blank=True, null=True)

    # Great Vessels
    aorta = models.PositiveSmallIntegerField(choices=aorta_choices,blank=True, null=True)
    pulmonary_artery = models.PositiveSmallIntegerField(choices=pulmonary_artery_choices,blank=True, null=True)
    ias = models.PositiveSmallIntegerField(choices=ias_choices,blank=True,null=True)
    ivs = models.PositiveSmallIntegerField(choices=ivs_choices,blank=True,null=True)
    mass_device = models.PositiveSmallIntegerField(choices=mass_device_choices,blank=True, null=True)
    massdevice_description = models.TextField(blank=True,null=True)
    pericardium = models.PositiveSmallIntegerField(choices=pericardium_choices,blank=True,null=True)
    pericardium_description = models.TextField(blank=True,null=True)

    # LV Dimension
    lv_diastolic_diameter = models.DecimalField(decimal_places=1,max_digits=100,null=True, blank=True)
    lv_diastolic_diameter_bsa = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    lv_systolic_diameter = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    lv_systolic_diameter_bsa = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)

    # LV Volume
    lv_diastolic_volume = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    lv_diastolic_volume_bsa = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    lv_systolic_volume = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    lv_systolic_volume_bsa = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)

    # LV Function
    lv_ef = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)

    # LV Mass by Linear Method
    septal_wall_thickness = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    posterior_wall_thickness = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    lv_mass = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    lv_mass_bsa = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)

    # LV Mass by 2D Method
    lv_mass_2d_method = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    lv_mass_bsa_2d_method = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)

    rv_basal_diameter = models.DecimalField(decimal_places=1, max_digits=100,null=True, blank=True)
    rv_mid_diameter = models.DecimalField(decimal_places=1, max_digits=100,null=True, blank=True)

    annulus = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    sinuses_of_valsalva = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)

    sinotublar_junction = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    proximal_ascending_aorta = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)

    lv_mass_linear_method = models.DecimalField(decimal_places=1, max_digits=100,null=True, blank=True)
    lv_mass_bsa_linear_method = models.DecimalField(decimal_places=1, max_digits=100,null=True, blank=True)

    # LV internal dimension
    # diastolic_dimension = models.DecimalField(decimal_places=1, max_digits=100, null=True)
    # systolic_dimension = models.DecimalField(decimal_places=1, max_digits=100, null=True)

    # LV Volumes
    # lv_edv = models.DecimalField(decimal_places=1, max_digits=100, null=True)
    # lv_esv = models.DecimalField(decimal_places=1, max_digits=100, null=True)
    # ap_dimension = models.DecimalField(decimal_places=1, max_digits=100, null=True)
    # ap_dimension_index = models.DecimalField(decimal_places=1, max_digits=100, null=True)

    # 17-Segment left ventricular Map
    basal_anterior = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    basal_anteroseptal = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    basal_inferoseptal = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    basal_inferior = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    basal_inferolateral = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    basal_anterolateral = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    mid_anterior = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    mid_anteroseptal = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    mid_inferoseptal = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    mid_inferior = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    mid_inferolateral = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    mid_anterolateral = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    apical_anterior = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    apical_septal = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    apical_inferior = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    apical_lateral = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    apex = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)

    # MVG
    mvg_peak = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    mvg_mean = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)

    # AVG
    avg_peak = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)
    avg_mean = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)

    image_scan = models.ImageField(null=True,blank=True)
    pdf = models.FileField(blank=True,null=True)
    avi = models.FileField(blank=True,null=True)
    recommendation = models.SmallIntegerField(choices=RECOMMENDATION_CHOICES, blank=True, null=True)
    flagged = models.IntegerField(choices=FLAGGED_CHOICES,blank=True,null=True)
    # flagged_fields = ArrayField(models.CharField(max_length=200,null=True,blank=True),null=True,blank=True)
    @property
    def bsa(obj):
        return math.sqrt(obj.height * obj.weight / 3600)

    @property
    def bmi(obj):
        return (obj.weight / pow(obj.height, 2))

    @property
    def segments_average(obj):
        sum = obj.basal_anterior+obj.basal_anteroseptal+obj.basal_inferoseptal+obj.basal_inferior+obj.basal_inferolateral+obj.basal_anterolateral+obj.mid_anterior+obj.mid_anteroseptal+obj.mid_inferoseptal+obj.mid_inferior+obj.mid_inferolateral+obj.mid_anterolateral+obj.apical_anterior+obj.apical_septal+obj.apical_inferior+obj.apical_lateral
        return sum/17

    def __str__(self):
        return f'Study Details for {self.id}'



class Case(TimeStamp, models.Model):
    STATUS_CHOICES = (
        (1, 'Waiting'),
        (2, 'Handled'),
        (3,'Assigned')
    )
    COMPLAINT_CHOICES = (
        (1,'Chest Pain'),
        (2,'Dyspnea'),
        (3,'Palpitation'),
        (4,'Cyanosis')
    )

    client = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False, related_name='cases')
    description = models.TextField(max_length=150, blank=True, null=True)
    technician = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False,
                                   related_name='case_technicians')
    reporting_md = models.ForeignKey(MedicalDoctor, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='reporting_md_set')
    referring_md = models.ForeignKey(MedicalDoctor, blank=True, null=True, on_delete=models.DO_NOTHING,
                                     related_name='referring_md')
    status = models.PositiveSmallIntegerField(default=1, choices=STATUS_CHOICES, blank=True, null=True)
    complaint_selected = models.PositiveSmallIntegerField(choices=COMPLAINT_CHOICES,null=True,blank=True)
    complaint_description = models.CharField(max_length=300,null=True,blank=True)
    related_study = models.OneToOneField(Study, on_delete=models.CASCADE,null=True, blank=True,related_name='related_study_set')

    def __str__(self) -> str:
        return f'case {self.id} {self.client}'
    
class TWaveMorphologyOptions(models.Model):
    option = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.option

class StSegmentOptions(models.Model):
    option = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.option
    
class StudyQualityOptions(models.Model):
    option = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.option

class StSegmentElevation(models.Model):
    option = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.option

class StSegmentDepression(models.Model):
    option = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.option

class Location(models.Model):
    option = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.option

class Echo(TimeStamp,models.Model):
    AVB_CHOICES = (
        (1, '1 AVB'),
        (2, '2 AVB TYPE I'),
        (3, '2 AVB TYPE II'),
        (4, 'CHB')
    )
    PWAVE_APPEARANCE_CHOICES = (
        (1,'Normal'),
        (2,'Abnormal')
    )

    PR_INTERVAL_APPEARANCE_CHOICES = (
        (1,'Normal'),
        (2,'Shortened'),
        (3,'Prolonged')
    )

    QWAVE_APPEARANCE_CHOICES = (
        (1,'Absent'),
        (2,'Present')
    )

    MORPHOLOGY_CHOICES = (
        (1,'Pathologic'),
        (2,'No Pathologic')
    )

    LOCATION_CHOICES = (
        (1,'I'),
        (2,'II'),
        (3,'III'),
        (12,'aVR'),
        (4,'aVL'),
        (5,'aVF'),
        (6,'V1'),
        (7,'V2'),
        (8,'V3'),
        (9,'V4'),
        (10,'V5'),
        (11,'V6')
    )

    QRS_MORPHOLOGY_CHOICES = (
        (1,'Narrow'),
        (2,'Broad')
    )

    QRS_HEIGHT_CHOICES = (
        (1,'Normal'),
        (2,'LVH'),
        (3,'RVH')
    )

    QRS_PATTERN_CHOICES = (
        (1,'Normal'),
        (2,'RBBB'),
        (3,'LBBB')
    )

    ST_SEGMENT_ELEVATION_CHOICES = (
            (1, 'I'),
            (2, 'II'),
            (3, 'III'),
            (12,'aVR'),
            (4, 'aVL'),
            (5, 'aVF'),
            (6, 'V1'),
            (7, 'V2'),
            (8, 'V3'),
            (9, 'V4'),
            (10, 'V5'),
            (11, 'V6')
    )

    T_WAVE_MORPHOLOGY_CHOICES = (
        (1,'Normal'),
        (2, 'Inversion I'),
        (3, 'Inversion II'),
        (4, 'Inversion III'),
        (5, 'Inversion aVL'),
        (6, 'Inversion aVF'),
        (7, 'Inversion V1'),
        (8, 'Inversion V2'),
        (9, 'Inversion V3'),
        (10, 'Inversion V4'),
        (11, 'Inversion V5'),
        (12, 'Inversion V6')
    )

    STRAIN_PROBLEM_CHOICES = (
        (1,'No'),
        (2,'Left Side'),
        (3,'Right Side')
    )

    FLAGGED_CHOICES = (
        (0,"False"),
        (1,"True")
    )
    YES_OR_NO_CHOICE = (
        (1,"Yes"),
        (2,"No")
    )
    AXIS_CHOICES = (
        (1,"Normal"),
        (2,"Right Axis Deviation"),
        (3,"Left Axis Deviation")
    )

    ST_SEGMENT_CHOICES = (
        (1,"Normal"),
        (2,"ST Segment Elevation"),
        (3,"ST Segment Depression")
    )

    patient = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='echos')
    reason_for_test = models.CharField(max_length=300,blank=True,null=True)
    referring_md = models.ForeignKey(MedicalDoctor, blank=True, null=True, on_delete=models.DO_NOTHING,
                                     related_name='echo_referring_md')
    rate = models.IntegerField(blank=True,null=True)

    # Rhythm
    nsr = models.IntegerField(choices=YES_OR_NO_CHOICE,blank=True,null=True)
    sinus_tachycardia = models.IntegerField(choices=YES_OR_NO_CHOICE,blank=True,null=True)
    sinus_bradycardia = models.IntegerField(choices=YES_OR_NO_CHOICE,blank=True,null=True)
    atrial_bradycardia = models.IntegerField(choices=YES_OR_NO_CHOICE,blank=True,null=True)
    supraventricular_bradycardia = models.IntegerField(choices=YES_OR_NO_CHOICE,blank=True,null=True)

    narrow_qs_tachycardia = models.IntegerField(choices=YES_OR_NO_CHOICE,blank=True,null=True)
    wide_qs_tachycardia = models.IntegerField(choices=YES_OR_NO_CHOICE,blank=True, null=True)
    vt = models.IntegerField(choices=YES_OR_NO_CHOICE,blank=True, null=True)
    vf = models.IntegerField(choices=YES_OR_NO_CHOICE,blank=True, null=True)
    avb = models.PositiveSmallIntegerField(choices=AVB_CHOICES, blank=True, null=True)

    # Axis
    axis = models.SmallIntegerField(choices=AXIS_CHOICES,null=True,blank=True)

    # P Wave
    p_wave_appearance = models.PositiveSmallIntegerField(choices=PWAVE_APPEARANCE_CHOICES, blank=True, null=True)

    # Q Wave
    q_wave_appearance = models.PositiveSmallIntegerField(choices=QWAVE_APPEARANCE_CHOICES, blank=True, null=True)
    q_wave_morphology = models.PositiveSmallIntegerField(choices=MORPHOLOGY_CHOICES, blank=True, null=True)
    location = models.ManyToManyField(Location,blank=True, related_name='location_set', null=True)

    # QRS Complex
    qrs_morphology = models.PositiveSmallIntegerField(choices=QRS_MORPHOLOGY_CHOICES, blank=True, null=True)
    qrs_height = models.PositiveSmallIntegerField(choices=QRS_HEIGHT_CHOICES, blank=True, null=True)
    qrs_pattern = models.PositiveSmallIntegerField(choices=QRS_PATTERN_CHOICES, blank=True, null=True)

    #ST Segment
    st_segment = models.ManyToManyField(StSegmentOptions,blank=True,related_name="stsegment_options", null=True)
    st_segment_elevation = models.ManyToManyField('StSegmentElevation',blank=True,related_name="st_segment", null=True)
    st_segment_depression = models.ManyToManyField('StSegmentDepression',blank=True,related_name="st_segment", null=True)


    #T Wave
    t_wave_morphology = models.ManyToManyField(TWaveMorphologyOptions, blank=True, null=True, related_name='t_wave_morphology_set')
    strain_problem = models.PositiveSmallIntegerField(choices=STRAIN_PROBLEM_CHOICES, blank=True,null=True)

    #QT corrected Interval
    qt = models.IntegerField(blank=True, null=True)

    flagged = models.SmallIntegerField(choices=FLAGGED_CHOICES,blank=True,null=True)
    # flagged_fields = ArrayField(models.CharField(max_length=200,null=True,blank=True),null=True,blank=True)

    description = models.TextField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True)
    video = models.FileField(blank=True,null=True)

    def __str__(self):
        return f'Electrocardiogram # {self.patient}'
