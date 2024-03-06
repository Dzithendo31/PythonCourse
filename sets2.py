outdoor_activities = {'Hiking', 'Cycling', 'Swimming'}
indoor_activities = {'Gaming', 'Reading', 'Cycling'}
activity_gadgets = {'Smartwatch': 'Hiking', 'VR Headset': 'Gaming', 'Smartphone': 'Reading', 'Drone': 'Cycling'}


#which one are outdoor gadgets? as set or List

out_gad = set()
in_gad = set()
for gadget in activity_gadgets:
  if (activity_gadgets[gadget] in outdoor_activities):
    out_gad.add(gadget)
  elif (activity_gadgets[gadget] in indoor_activities):
    in_gad.add(gadget)

print(out_gad)
print(in_gad)

#Think of another way 
#{}
def findGad(activity_gadgets,activities):
  gadgets = set()
  for gadget in activity_gadgets:
    if (activity_gadgets[gadget] in activities):
      gadgets.add(gadget)
  return gadgets

print(findGad(activity_gadgets,indoor_activities))
#Create two empty
def get_activity_gadgets(activity_gadgets, activity_list):
  return set([gadget for gadget, activity in activity_gadgets.items() 
              if activity in activity_list])

def findGad2(activity_gadgets,activities):
  return set([gadget for gadget, activity in activity_gadgets.items()
             if activity in activities])

print(findGad2(activity_gadgets,indoor_activities))

#lambda functions, Cuter and Nicer

