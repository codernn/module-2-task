import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Realtimealert {
    public static void main(String[] args) throws IOException {
        final BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        try{
            for (;;) {
                try{    
                    String[] line = bufferedReader.readLine().split(",");
                    if(line.length==4){
                        try{
                            final int SERVER_ID = Integer.parseInt(line[0]);
                            final int CPU_UTILIZATION = Integer.parseInt(line[1]);
                            final int MEMORY_UTILIZATION = Integer.parseInt(line[2]);
                            final int DISK_UTILIZATION = Integer.parseInt(line[3]);
                            if(CPU_UTILIZATION > 85 || MEMORY_UTILIZATION > 75 || DISK_UTILIZATION > 60){
                                    System.out.print("Alert, "+SERVER_ID);
                                    if(CPU_UTILIZATION > 85){
                                        System.out.print(", CPU_UTILIZATION VIOLATED");
                                    }
                                    if( MEMORY_UTILIZATION > 75 ){
                                        System.out.print(", MEMORY_UTILIZATION VIOLATED");
                                    }
                                    if( DISK_UTILIZATION > 75 ){
                                        System.out.print(", DISK_UTILIZATION VIOLATED");
                                    }
                                    System.out.print("\n");
                            }
                            else{
                                System.out.println("No Alert,"+SERVER_ID);
                            }
                        }
                        catch(NumberFormatException n){
                            System.out.println("The format is not correct");
                        }
                    }
                    else{
                        System.out.println("The format is not correct");
                    }
                }
                catch(ArrayIndexOutOfBoundsException e){
                    System.out.println("The format is not correct");
                }
            }
        }
        catch(NullPointerException e){
            System.out.println("No Input given");
        }
    }
}
