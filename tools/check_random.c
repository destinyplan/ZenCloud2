#include <stdio.h>
#include <time.h>
//作业荣誉颁奖典礼优选程序V1.0
//author：all
#include <stdbool.h>
#include <math.h>

#define LIMIT_NUM 10

void CheckSomebody2Speak(int num)
{
	time_t t;
	int n = 0;
	int list[num];
	int index=0;

	srand((unsigned) time(&t));

	printf("恭喜以下幸运观众:");
	while(1)
	{
		n=rand()%(LIMIT_NUM+1);
		bool isSame=false;
		for(int i=0;i<num;i++)
		{
			if(list[i]==n)
			{
				isSame=true;
				break;
			}
		}
		if(isSame)
		{
			continue;
		}
		list[index]=n;
		index++;
		if(num<=index)
		{
			break;
		}	
	}

	for(int i=0;i<num;i++)
	{
		printf(" %d ,",list[i]);
	}
	printf("号，请开始你的表演!!!\n");
	
//	return n+1;
}

int main()
{
	int num=0;
	while(1)
	{
		printf("你想要几个倒霉蛋:");
		scanf("%d",&num);
		if(num>0 && num <=LIMIT_NUM)
		{
			CheckSomebody2Speak(num);
			break;	
		}else
		{
			printf("your input num is error,please input again and be smart!boy!\n");
			continue;
		}
	}
}






