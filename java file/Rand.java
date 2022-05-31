public class Rand {
    public static int[] rand(int[] tab , int maxmot) {
        double g;
        for (int i = 0 ; i < maxmot ; i++){
            g = Math.random() * 100;
            tab[i]= (int)g ;    
            System.out.println(tab[i]);
        }
        return tab;
    }
}
