public class Loops {
    public static void main(String[] args) {
        // System.out.println("Hello Melissa!");
        // forLoop();
        // whileLoop();
        //  doWhileLoop("Sooreoluwa", "Melissa");
        String[] items ={"Mango", "Pineapple", "Orange"};
        forEachLoop(items);
    }
 

   static void forLoop(){
        for (int n = 1; n < 5; n++){
        System.out.println("Hello Melissa!");
        }
    }

      static void whileLoop(){
        String mentee = "Melissa";
        String mentor = "Sooreoluwa";
        while (mentor != mentee){
        System.out.println("Tutorial!");
        }
    }

    static void doWhileLoop(String mentor, String mentee){
        // String mentee = "Melissa";
        // String mentor = "Sooreoluwa";
        do {
            System.out.println(mentor + " & " + mentee);
        }
        while (mentor == mentee);
    }

    static void forEachLoop(String[] items){
        for(String item : items){
            System.out.println( "This is a " + item);
        }
    }
}

