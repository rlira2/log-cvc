process_steps = [
    ("Preparation of operator and patient","Prepararción Operador y Paciente"),
    ("Preparation of ultrasound equipment","Preparación Equipo Ultrasonido"),
    ("Locate structures","Localizar Estructuras"),
    ("Venous Puncture","Punción de la Vena"),
    ("Guidewire install","Instalación de la Guía"),
    ("Catheter install","Instalación Catéter"),
    ("Catheter fixation","Fijación Catéter")
]

activities_english = [
    ("Prepare implements", "Preparation of operator and patient"),
    ("Perform surgical hand washing", "Preparation of operator and patient"),
    ("Gets in sterile gown,  gloves,  hat and mask","Preparation of operator and patient" ),
    ("Clean puncture area with chlorhexidine", "Preparation of operator and patient"),
    ("Drap puncture area in sterile fashion", "Preparation of operator and patient"),
    ("Ultrasound setup (deep and vascular mode)", "Preparation of ultrasound equipment"),
    ("Puts gel in probe", "Preparation of ultrasound equipment"),
    ("Cover sterile probe", "Preparation of ultrasound equipment"),
    ("Put sterile gel", "Preparation of ultrasound equipment"),
    ("Probe position at puncture zone", "Preparation of ultrasound equipment"),
    ("To give position to the patient", "Locate structures"),
    ("Anatomical vein identification", "Locate structures"),
    ("Identificate vein with color doppler", "Locate structures"),
    ("Compression test Identification", "Locate structures"),
    ("Anesthetize puncture zone", "Venous Puncture"),
    ("Vein puncture with trocar under ultrasound vision", "Venous Puncture"),
    ("Venous blood return +", "Venous Puncture"),
    ("Drop probe and put in sterile area", "Guidewire install"),
    ("Remove syringe from the puncture trocar", "Guidewire install"),
    ("Advance seldinger guidewire from puncture trocar", "Guidewire install"),
    ("Remove puncture trocar", "Guidewire install"),
    ("Check guidewire position in to the vein in short axis", "Guidewire install"),
    ("Check guidewire position in to the vein in long axis", "Guidewire install"),
    ("Guidewire in good position (into the vein)", "Guidewire install"),
    ("Widen subcutaneous pathway", "Catheter install"),
    ("Advance catheter over guideware whithout lose control of there", "Catheter install"),
    ("Remove guidewire entirety", "Catheter install"),
    ("Check flow and reflow from catheter each port", "Catheter install"),
    ("Catheter in good position (into the vein)", "Catheter install"),
    ("Secure the catheter in place", "Catheter fixation"),
    ("Put catheter patches", "Catheter fixation"),
    ("Check catheter position with radiology method", "Catheter fixation")
]

activities_spanish = [
    ("Preparar implementos", "Prepararción Operador y Paciente"),
    ("Realizar lavado de manos quirúrgico", "Prepararción Operador y Paciente"),
    ("Vestirse con guantes, sombrero y máscara estériles", "Prepararción Operador y Paciente"),
    ("Limpiar el área de punción con clorhexidina", "Prepararción Operador y Paciente"),
    ("Colocar paños estériles", "Prepararción Operador y Paciente"),
    ("Configurar ultrasonido (modo profundo y vascular)", "Preparación Equipo Ultrasonido"),
    ("Poner gel en el transductor", "Preparación Equipo Ultrasonido"),
    ("Cubrir transductor estéril", "Preparación Equipo Ultrasonido"),
    ("Poner gel estéril", "Preparación Equipo Ultrasonido"),
    ("Posicionar transductor en la zona de punción", "Preparación Equipo Ultrasonido"),
    ("Posicionar al paciente", "Localizar Estructuras"),
    ("Identificar anatómicamente la vena", "Localizar Estructuras"),
    ("Identificar la vena con color Doppler", "Localizar Estructuras"),
    ("Identificar la vena con test de compresión", "Localizar Estructuras"),
    ("Anestesiar zona de punción", "Punción de la Vena"),
    ("Punción de la vena con trócar bajo visión de ultrasonido", "Punción de la Vena"),
    ("Aspirar retorno de sangre", "Punción de la Vena"),
    ("Soltar transductor y dejarlo en área estéril", "Instalación de la Guía"),
    ("Retirar la jeringa del trócar de punción", "Instalación de la Guía"),
    ("Pasar guía de Seldinger por trócar", "Instalación de la Guía"),
    ("Retirrar trócar de punción", "Instalación de la Guía"),
    ("Verificar la posición de la  guía en la vena con el eje corto", "Instalación de la Guía"),
    ("Verificar la posición de la  guía en la vena con el eje largo", "Instalación de la Guía"),
    ("Guía en buena posición (en la vena)", "Instalación de la Guía"),
    ("Ampliar la vía subcutánea", "Instalación Catéter"),
    ("Avanzar el catéter sobre la guía sin perder el control", "Instalación Catéter"),
    ("Retirar la guía entera", "Instalación Catéter"),
    ("Verificar el flujo y reflujo del catéter en cada puerto", "Instalación Catéter"),
    ("Catéter en buena posición (en la vena)", "Instalación Catéter"),
    ("Asegurar el catéter en su lugar", "Fijación Catéter"),
    ("Colocar parches de catéter", "Fijación Catéter"),
    ("verificar la posición del catéter con el método de radiología", "Fijación Catéter"),
]

print ("\nTHE STEPS OF THE PROCESS ARE:")
for english_step in process_steps:
    print (english_step[0])

print ("\nLAS ETAPAS DEL PROCESO SON:")
for spanish_step in process_steps:
    print (spanish_step[1])

print ("\nTHE ACTIVITIES OF THE PROCESS ARE:")
for english_activity in activities_english:
    print (english_activity[0])

print ("\nLAS ACTIVIDADES DEL PROCESO SON:")
for spanish_activity in activities_spanish:
    print (spanish_activity[0])