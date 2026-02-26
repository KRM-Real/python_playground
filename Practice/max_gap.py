def maximumGap(self, nums):
        
        if len(nums) < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)

        if min_val == max_val:
            return 0

        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = ((max_val - min_val) // bucket_size) + 1

        buckets = [[None, None] for _ in range(bucket_count)]

        for num in nums:
            index = (num - min_val) // bucket_size

            if buckets[index][0] is None:
                buckets[index][0] = buckets[index][1] = num
            else:
                buckets[index][0] = min(buckets[index][0], num)
                buckets[index][1] = max(buckets[index][1], num)

        max_gap = 0
        prev_max = min_val

        for bucket in buckets:
            if bucket[0] is None:
                continue

            max_gap = max(max_gap, bucket[0] - prev_max)
            prev_max = bucket[1]

        return max_gap
