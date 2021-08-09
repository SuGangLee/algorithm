package 알고리즘;

import java.util.Scanner;

public class 소수판정 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		int s=0;
		int l=0;
		int tmp=0,count=0;
		s=scan.nextInt();
		l=scan.nextInt();

		if(s>l)
		{	tmp=s; s=l; l=tmp;
		}
		boolean[] sqrt=new boolean[l]; // 소수판정을 위한 배
		
		int root = (int)Math.pow(l, 0.5); // 제곱근의 값만 비
		
		for(int i=0;i<sqrt.length;i++) {sqrt[i]=true;} // 소수판정 초기
		
		for(int i=2;i<root;i++) {
			 
				for(int j=2;j*i<l;j++)
				{ 
					sqrt[j*i]=false; //소수의배수들을 모두 false로 치환
				}
			}
		
		for(int i=s,j=1; i<l;i++) {
			if (sqrt[i]==true ) {System.out.print(i+"  "); ++count;} //소수들만 출력, 10개단위, s보다 큰 범위
			else continue;
			if(count==10*j) {System.out.println();j++;}
			
		}
		System.out.println();
		System.out.println();
		System.out.println(count); // 총개수 반
	}

}
