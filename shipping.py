#Declare variables
weight = 41.5
premium_ground = 125.00

#Ground Shipping
if weight <= 2.0:
  cost_ground = (weight * 1.50) + 20
elif weight >= 2.0 and weight <= 6.0:
  cost_ground = (weight * 3.00) + 20
elif weight >= 6.0 and weight <= 10.0:
  cost_ground = (weight * 4.00) + 20
else:
  cost_ground = (weight * 4.75) + 20

#Print out the Ground Shipping cost
print(f"The cost for Ground Shipping is:  ${cost_ground}")
print(f"\nThe cost for Premium Ground Shipping is:  ${premium_ground}")

#Drone Shipping
if weight <= 2.0:
  cost_drone = weight * 4.50
elif weight >= 2.0 and weight <= 6.0:
  cost_drone = weight * 9.00
elif weight >= 6.0 and weight <= 10.0:
 cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

#Print out the Drone Shipping cost
print(f"\nThe cost for Drone Shipping is:  ${cost_drone}")


#Print out the cheapest method of shipping
if cost_ground < premium_ground and cost_ground < cost_drone:
  print(f"\nGround Shipping is the cheapest:  ${cost_ground}")
elif premium_ground < cost_ground and premium_ground < cost_drone:
  print(f"\nPremium Shipping is the cheapest:  ${premium_ground}")
elif cost_drone < premium_ground and cost_drone < cost_ground:
  print(f"\nDrone Shipping is the cheapest method of shipping:  ${cost_drone}")
else:
  print(f"\nThe shipping costs are equal")


'''
#Ground Shipping
if weight <= 2.0:
  cost_ground = 125
elif weight >= 2.0 and weight <= 6.0:
  cost_ground = 125
elif weight >= 6.0 and weight <= 10.0:
  cost_ground = 125
else:
  cost_ground = 125

#Print out the Ground Shipping cost
print(f"The cost for Ground Shipping is:  ${cost_ground}")
print(f"\nThe cost for Premium Ground Shipping is:  ${premium_ground}")

#Drone Shipping
if weight <= 2.0:
  cost_drone = 125
elif weight >= 2.0 and weight <= 6.0:
  cost_drone = 125
elif weight >= 6.0 and weight <= 10.0:
 cost_drone = 125
else:
  cost_drone = 125

#Print out the Drone Shipping cost
print(f"\nThe cost for Drone Shipping is:  ${cost_drone}")
'''