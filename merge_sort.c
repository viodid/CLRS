#include<stdio.h>

int merge_sort(int Arr[], int n);

int main(){
	int Arr[5] = {1,2,3,4,5};
	merge_sort(Arr, 5); 
	return 0;
}

int merge_sort(int Arr[], int n){
	
	if (n <= 1)
	{
		return 0;
	}
	
	int middle;
	if (n % 2 != 0) 
	{	
		middle = (n - 1) / 2;
	
	} 
	else 
	{
		middle = n / 2;		
	}
	
	int left[middle];
	int right[n - middle];
	for (int i = 0; i < middle; i++)
	{
		left[i] = Arr[i];
	}
	for (int i = 0; i < (n - middle); i++)
	{
		right[i] = Arr[middle + i];
		printf("%i\n", right[i]);
	}
	merge_sort(left, middle);
	merge_sort(right, (n - middle));
	

	return 0;
}





