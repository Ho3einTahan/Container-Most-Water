def max_area(height):
   
   left=0
   right=len(height)-1
   max_water=0
   
   while left<right:
      
      # height
      h=min(height[left],height[right])
      
      # width
      w=right-left
      
      # area
      current=h*w
      
      max_water=max(max_water,current)
      
      if height[left]<height[right]:
         left+=1
      else:
         right-=1
         
   return max_water
      



print(max_area([2,10,4,20,8,10,5,4]))