import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Random;

public class NumberGuessing {
    public static void main(String[] agrs){
        Random rand = new Random();
        int compNum = rand.nextInt(200) + 1;
        BufferedReader br = null;
        
        System.out.println("Guess a number between 0 to 200:");
        try {
            br = new BufferedReader(new InputStreamReader(System.in));
            
            while (true){
                int guess = Integer.parseInt(br.readLine());
                //System.out.println("you guessed" + guess);
                if (guess == compNum){
                    System.out.println("Good guess !");
                    break;
                } else if (guess < compNum){
                    System.out.println(guess + " is too small, please guess again:");
                } else {
                    System.out.println(guess + " is too big, please guess again:");
                }
            }
            
        } catch (IOException e) {
            e.printStackTrace();
        } finally{
            System.out.println("finally");
        }
    }
}


