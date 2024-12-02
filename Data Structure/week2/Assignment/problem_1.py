def find_nearest_temperature(sorted_temps, target_temp):
    if not sorted_temps:
        return None
    
    left=0
    right=len(sorted_temps)-1
    while right-left>1:
        mid=(left+right)//2
        if sorted_temps[mid]==target_temp:
            return target_temp
        elif sorted_temps[mid]<target_temp:
            left=mid
        else:
            right=mid

    if abs(sorted_temps[right]-target_temp)<abs(target_temp-sorted_temps[left]):
        answer=sorted_temps[right]
    else:
        answer=sorted_temps[left]

    return answer
    


def main():
    sorted_temps = [-20, -15, -5, 3, 8, 12, 30, 45, 50, 60]
    target_temp = 7

    nearest = find_nearest_temperature(sorted_temps, target_temp)
    print(nearest)  # Should print 8


if __name__ == "__main__":
    main()
