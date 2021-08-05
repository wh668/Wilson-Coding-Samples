import java.util.Scanner;
public class Lab2 {
	
	/* This is a simple project with the goal of converting units (feet/pounds)
	 * and calculating a gratuity/total. Note that there is no exception handling and it is
	 * anticipated the user inputs correct values. 
	 */
	
public static void main(String[] args){
		
		// First problem (Feet to meters)
		 
		// Declare variables 
		float feet;
		
		float feetToMeterUnit; 
		
		Scanner userData= new Scanner(System.in);
		System.out.println("Enter number in feet: ");
		feet= userData.nextFloat();
		
		// Unit conversion 
		float meter;
		meter= .305f * feet; 
		
		
		System.out.println(feet + " feet is " + meter + " meters");
		
		
		// Second problem (pounds to kilogrmas)
		
		// Declare variables 
		float pound;
		
		float poundToKilogramUnit;
		
		Scanner userData1= new Scanner(System.in);
		System.out.println("Enter number in pounds: ");
		pound= userData1.nextFloat();
		
		// Unit conversion 
		float kilogram;
		kilogram= .454f * pound;
				
		System.out.println( pound + " pound(s) are " + kilogram + " kilograms");
		
		
		// Third problem (Subtotal)

		//Declare variables 
		float gratuityrate; 
		float subtotal;
		Scanner userData2= new Scanner(System.in);

		System.out.println("Enter the subtotal rounded to the nearest penny: ");
		subtotal= userData2.nextFloat();
		
		System.out.println("Enter the gratuity rate as a percentage: ");
		gratuityrate= userData2.nextFloat();
		
		// Gratuity/Total calculations 
		double total;
		total= (gratuityrate/100 * subtotal) + subtotal;
		total= 	Math.round(total* 100.0)/100.0;
		
		double gratuity;
		gratuity= gratuityrate/100 * subtotal;
		gratuity= Math.round(gratuity * 100.0) /100.0;
		
		System.out.println(" The gratuity is " + gratuity + " dollars and the total is " + total + " dollars");
				
				
		
	}

}

