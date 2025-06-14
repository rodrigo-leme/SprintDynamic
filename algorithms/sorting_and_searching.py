class SortingAndSearching:
 
    def _quick_sort(self, arr, low, high):
        """implementação do Quick Sort"""
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort(arr, low, pi - 1)
            self._quick_sort(arr, pi + 1, high)
    
    def _partition(self, arr, low, high):
        """função de partição para Quick Sort"""
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def _merge_sort(self, arr):
        """implementação do Merge Sort"""
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            
            self._merge_sort(left)
            self._merge_sort(right)
            
            i = j = k = 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
    
    def _busca_binaria(self, arr, x):
        """implementação da Busca Binária"""
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1 