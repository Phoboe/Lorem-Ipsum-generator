import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Rentrez le nombre de mot :");
        int maxmot = scanner.nextInt() , rando;
        List liste_mot = new ArrayList();
        String produit_fini = new String();
        int val_sauv = 0 ;

        List<List<String>> records = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader("LoremIpsum"))) { // Lorem ipsum 150 paragraphs.txt
            String line;
            while ((line = br.readLine()) != null) {
                String[] values = line.split(","); // " "
                records.add(Arrays.asList(values));
            }
        }
        catch (Exception e){
        }

        //System.out.println(records);
        
        for (int i = 0 ; i < records.size() ; i++ ){
            for (int j = 0 ; j < records.get(i).size() ; j++ ){
                liste_mot.add(records.get(i).get(j));
            }
        }


        for( int i = 0 ; i < maxmot ; i++ ){
            rando = Rand.rand(0, liste_mot.size(),val_sauv);
            produit_fini += liste_mot.get(rando)+" ";
            val_sauv = liste_mot.indexOf(liste_mot.get(rando));
        }

        //System.out.println(liste_mot);

        System.out.println(produit_fini);
    }   
}