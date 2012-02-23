class TwinPrime{

public static void main (String [] args)
{
	for (int i=2; ;i++ ){
		if(checkPrime(i)){
			if(checkPrime(i+2)){
				int j=i+2;
				System.out.println(i + " "+j);
			}
		} 
	}
}
public static  boolean checkPrime(int number){
	for (int i=2;i<=number/2;i++)
		if ((number%i)==0){
			return false;
		}
	return true;
	}
}


