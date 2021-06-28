import java.io.*;
import java.util.StringTokenizer;
public class Main {
	static sys io = new sys();
	public static void main(String[] args) {
		/*
		Code
		*/
		io.close();
	}
	public static int count(String word, char character) {
	    int count = 0;
	    for(int i = 0; i <= word.length(); i++) {
	        try {
    	        if(word.charAt(i) == character) {
    	            count++;
    	        }
	        } catch(Exception e) {}
	    }
	    return count;
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
	public char nextChar() { return next().charAt(0); }
}
