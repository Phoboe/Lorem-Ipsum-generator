public class main {

    public static void main(String[] args) {
        int maxmot = 10;
        int taille = 10;
        int rando , x , y , z;
        int nb_de_mot = 1000000;
        String[] dico = new String[]{"he","ha","hi"};
        String produit_fini = new String();
        
        rando = Rand.rand();
        for( int i = 0 ; i < maxmot ; i++ ){
            if(rando <= 3) {
                produit_fini += dico[0] + " ";
            }
            else if (rando > 3 && rando <= 6){
                produit_fini += dico[1] + " ";
            }
            else if (rando > 6 && rando <= 10){
                produit_fini += dico[2] + " ";
            }
            rando = Rand.rand();
        }

        System.out.println(produit_fini);
    }   
}