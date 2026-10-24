class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            # Partition indices
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i

            # Boundary values around partition
            max_left1 = float('-inf') if i == 0 else nums1[i - 1]
            min_right1 = float('inf') if i == m else nums1[i]

            max_left2 = float('-inf') if j == 0 else nums2[j - 1]
            min_right2 = float('inf') if j == n else nums2[j]

            # Check if partition is valid
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Odd total length: median is max of left elements
                if (m + n) % 2 == 1:
                    return float(max(max_left1, max_left2))
                # Even total length: average of the two middle elements
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
            elif max_left1 > min_right2:
                # Too far right in nums1, move left
                high = i - 1
            else:
                # Too far left in nums1, move right
                low = i + 1

        return 0.0