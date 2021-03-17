import java.io.*;
class Main {
  public static void main(String[] args) throws IOException {  
    String x = input();
    String a = intinput();
    print(x);
    br.close();
    pw.close();
  }
  public static String input() {
    try{
      return br.readLine();
    } catch (IOException e) {
      e.printStackTrace();
    }
    return "error";
  }
  public static void print(String args) {
    pw.write(args + "\n");
  }
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static PrintWriter pw = new PrintWriter(System.out);
}
