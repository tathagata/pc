class Chap51{
	public static void main (String [] args)
	{
		System.out.println(Integer.toBinaryString(updateBin(1024,21,2,6)));	
	}

	public static int updateBin(int n, int m, int i, int j){
		System.out.println(Integer.toBinaryString(n)+", m="+ Integer.toBinaryString(m));
		int max = ~0;
		System.out.println(Integer.toBinaryString(max));
		System.out.println("left:"+Integer.toBinaryString(1<<j));
		int left = (1<<j)-1;System.out.println("left:"+Integer.toBinaryString(left));
		int right = (1<<i)-1;System.out.println("right:"+Integer.toBinaryString(right));
			System.out.println(left +" " +right);
		int mask = left | right;
		System.out.println("left OR right:"+ Integer.toBinaryString(left)+" " +Integer.toBinaryString(right)+ " "+Integer.toBinaryString(mask));			
		int nmasked=(n & mask);System.out.println("nmasked"+Integer.toBinaryString(nmasked));
		int mshifted = m <<i;System.out.println("mshifted"+Integer.toBinaryString(mshifted));
		return (nmasked|mshifted);
	}

}
