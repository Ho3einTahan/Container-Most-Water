def max_area(height):
   
   left=0
   right=len(height)-1
   max_water=0
   
   while left<right:
      
      h=min(height[left],height[right])
      w=right-left
      
      current=h*w
      
      max_water=max(max_water,current)
      
      if height[left]<height[right]:
         left+=1
      else:
         right-=1
   return max_water
      



print(max_area([2,10,4,20,8,10,5,4]))