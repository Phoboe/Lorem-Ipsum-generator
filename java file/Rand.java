public class Rand {
    public static int rand(int min , int max , int eviter){
        int range = max - min ;
        int h = 0;
        do {
        h = (int)(Math.random() * range) + min ;
        }while( h == eviter);
        return h;
    }
}
