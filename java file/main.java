import java.util.Scanner;

public class main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Rentrez le nombre de mot :");
        int maxmot = scanner.nextInt() , rando;
        String[] liste_mot = new String[]{"he","ha","hi"};
        String produit_fini = new String();
        
        for( int i = 0 ; i < maxmot ; i++ ){
            rando = Rand.rand(0, liste_mot.length);
            produit_fini += liste_mot[rando]+" ";
        }

        System.out.println(produit_fini);
    }   
}