import java.io.*;
import java.util.StringTokenizer;
public class Main {
	static sys io = new sys(); 
	public static void main(String[] args) {
		long n = io.nextLong(); // Taking the input as a long
		// When you submit you can look at the test cases, and by looking at the cases we can see that using an int causes us to get wrong answers or timeout errors.
		// This occurs due to the sheer size of the numbers.
		// So we use a long to alleviate these errors.
		String ans = String.valueOf(n); // Our answer variable is a String which we will concatenate to later.
		// String.valueOf(n) type castes n from a long to a String
		while(n != 1) { // We will be appending the value of n to ans and then changing n to the next value in the sequence. 
		// Since the sequence ends at 1, we keep going until n isn't 1.
		    n = n % 2 == 0 ? n / 2 : (n * 3) + 1; // If n is divisible by 2, n = n / 2, else n = (n * 3) + 1.
		    // This is using ternary in the place of an if-else conditional.
		    ans = ans + " " + String.valueOf(n);
		    // Concatenate our answer with a space and the new value of n.
		}
		io.print(ans); // Print ans
		io.close();
	}
}
class sys extends PrintWriter {
	private BufferedReader r;
	private StringTokenizer st;
	public sys() { this(System.in,System.out); }
	public sys(InputStream i, OutputStream o) {
		super(o);
		r = new BufferedReader(new InputStreamReader(i));
	}
	public String next() {
		try {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(r.readLine());
			return st.nextToken();
		} catch (Exception e) {}
		return null;
	}
	public int nextInt() { return Integer.parseInt(next()); }
	public double nextDouble() { return Double.parseDouble(next()); }
	public long nextLong() { return Long.parseLong(next()); }
	public boolean nextBool() { return Boolean.parseBoolean(next()); }
	public char nextChar() {
	    String value = next();
	    return value.charAt(0);
	}
}
