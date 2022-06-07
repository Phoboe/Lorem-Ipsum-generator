import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

public class main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Rentrez le nombre de mot :");
        int maxmot = scanner.nextInt() , rando;
        String[] liste_mot = new String[]{"he","ha","hi"};
        String produit_fini = new String();

        try (BufferedReader br = new BufferedReader(new FileReader("un fichier.csv"))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] values = line.split(",");
            }
            
        }
        catch (Exception e) {
            e.printStackTrace();
        }

        

        for( int i = 0 ; i < maxmot ; i++ ){
            rando = Rand.rand(0, liste_mot.length);
            produit_fini += liste_mot[rando]+" ";
        }

        System.out.println(produit_fini);
    }   
}