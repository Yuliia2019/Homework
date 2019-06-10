resting_pulse = int(raw_input("What is your resting pulse?"))
age = int(raw_input("What is your age?"))
print 'Resting pulse', ':', resting_pulse, 'Age', ':', age
for intensity in range(55, 96, 5):
    Pintensity = intensity/100.0
    print Pintensity
    TargetHeartRate = (((220 - age) - resting_pulse) * Pintensity) + resting_pulse
    print intensity, TargetHeartRate