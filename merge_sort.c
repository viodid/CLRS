#include<stdio.h>
#include<stdlib.h>

int merge_sort(int Arr[], int n);
void merge(int Arr[], int n, int _left[], int _right[], int middle);

int main(){
	int n = 7;
	int Arr[7] = {3,1,6,7,4,2,0};
	for (int i = 0; i < n; i++)
        {
                printf("%i,", Arr[i]);
        }
	merge_sort(Arr, n);
	printf("\n");
	for (int i = 0; i < n; i++)
	{
		printf("%i,", Arr[i]);
	}
	printf("\n");
	return 0;
}

int merge_sort(int Arr[], int n){
	
	// base case
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
	}
	merge_sort(left, middle);
	merge_sort(right, (n - middle));
	merge(Arr, n, left, right, middle);	

	return 0;
}

void merge(int Arr[], int n, int _left[], int _right[], int middle) 
{	
	// pointers to the repective subarrays
	int i = 0;
	int j = 0;

	int left[middle + 1];
	int right[n - middle + 1];

	for (int x = 0; x < middle; x++)
	{
		left[x] = _left[x];
	}
	left[middle+ 1] = -1;
	
	for (int z = 0; z < (n - middle); z++)
        {
                right[z] = _right[z];
        }
        right[n - middle + 1] = -1; 

	for (int k = 0; k < n; k++)
	{
		if (left[i] <= right[j])
		{
			Arr[k] = left[i];
			i++;
		}
		else
		{
			Arr[k] = right[j];
			j++;
		}

		if (left[i] == -1 || right[j] == -1)
		{
			while (right[j] != -1)
			{
				Arr[k] = right[j];
				k++;
				j++;
			}
			while (left[i] != -1)
                        {
                                Arr[k] = left[i];
                                k++;
                                i++;
                        }
			break;
		}
	}
	
}





