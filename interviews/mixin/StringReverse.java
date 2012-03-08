class StringReverse{
public static void chars ()
{
	String a = "was it a cat i saw";
	int alen = a.length()-1;
	String b = "";
	while (alen>=0){
		b += a.substring(alen,alen+1);
		alen--;
	} 
	System.out.println("reverse"+b);
}

public static void words ()
{
	String a = "was it a cat i saw";
	String b = "";
	int alen = a.length()-1;
	while (alen>=0){
		int i =alen;
		while(!(a.substring(i,i+1).equals(" "))&&(i>0)){
			i--;
		
		}
		if (i==0){
			b+= " " +a.substring(0,alen+1);
			break;
		}else{
			b+=a.substring(i,alen+1);
			alen=i-1;
		}
	}
	System.out.println("reverse"+b);
}
public static void main (String [] args)
{
	assert(args.length==5):args.length;
	words();
}
}
