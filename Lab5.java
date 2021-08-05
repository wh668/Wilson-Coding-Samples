import java.util.Scanner;
public class Lab5 {

	// Appx for pi using a convergence acceleration technique
	public static double piApproximation(int num){
		
		//Declaring/Initializing variables 
		double k;
		double total = (double) 2/3;
		
		// Accelerated Lebniz formula 
		for(k=1; k<= num; k++) {
			total += ( 2/((4*k+1)*(4*k+3)) );
		}
		
		/* Commented out is the Leibniz appx for pi (non convergence acceleration)
		 * for(k=1; k<= num; k++){
			if(k%2==0){
				total = total + 1/((2*k)+1);
			}
			else {
				total += -1/(2*k+1);
			}
		}
	*/
		return 4*total;
	}
	
	
	// Simple weight calculation using arbitrary rules for acceptable weight
	public static String CalculateWeight (double mass){
 
	
	double weight = mass *9.8;
	
	String tooHeavy = "Object too heavy";
	String tooLight = "Object too light";
	String normalWeight = "Object is of normal weight";
	
	if(weight>1000){
		return tooHeavy; 
	}
	else if(weight<10){
		return tooLight;
		
	}
	else{

		return normalWeight;
	}
		}
	
	
	
	
	public static float GymnasticsJudging(){
		Scanner input = new Scanner(System.in);
		float score = input.nextFloat();
		float counter = 0;
		float maximum = -100;
		for(counter=1; counter<=6; counter++){
			System.out.println("Enter score " + (counter+1) + ": ");
		score = input.nextFloat();
		if(score >= maximum){
			maximum = score;
			counter++;
			
			
		}
		
		}
		return score; 
		
	}
	

	
	
	
	
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
				
		Scanner DataSource = new Scanner(System.in);
		System.out.println("Enter number of terms: ");
		int terms;
		terms= DataSource.nextInt();
		
		double ValueComingBack;
		ValueComingBack= piApproximation (terms );
		System.out.println("The pi approx is " + ValueComingBack);
		
		
		
		Scanner DataSource1 = new Scanner(System.in);
		System.out.println("Enter object mass");
		double mass2 = DataSource1.nextDouble();
		
		String ValueReturning;
		ValueReturning = CalculateWeight(mass2);
		System.out.println(ValueReturning);
	}
	
	
	}
	



