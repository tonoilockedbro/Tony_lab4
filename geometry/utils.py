def area_stats(shapes):
   if not isinstance(shapes, list):
        raise TypeError("Input must be a list of shapes")
    
   area_list = [shape.area() for shape in shapes]
   return {
    "n": len(area_list),
    "total": sum(area_list),
    "mean": sum(area_list) / len(area_list) if area_list else 0,
    "min": min(area_list) if area_list else 0,
    "max": max(area_list) if area_list else 0,
    }

   