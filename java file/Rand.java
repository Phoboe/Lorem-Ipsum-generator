public class Rand {
    public static int rand(int min , int max){
        int range = max - min ,
        h = (int)(Math.random() * range) + min ;
        return h;
    }
}
