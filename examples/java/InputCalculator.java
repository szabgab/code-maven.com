import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class InputCalculator {
    public static void main(String[] args){
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("First number: ");
            int x = Integer.parseInt(br.readLine());
            System.out.print("Second number: ");
            int y = Integer.parseInt(br.readLine());
            System.out.print("Operator: ");
            String op = br.readLine();

            int z;

            if (op.equals("+")) {
                z = x+y;
            } else if (op.equals("-")){
                z = x-y;
            } else if (op.equals("*")){
                z = x*y;
            } else if (op.equals("/")){
                z = x/y;
            } else{
                 throw new java.lang.Error("Operator not recognized");
            }
            System.out.println("Result: " + z);

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}


