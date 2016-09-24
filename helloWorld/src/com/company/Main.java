package com.company;
import com.sun.imageio.plugins.common.BogusColorSpace;

import java.security.MessageDigest;
import  java.math.BigDecimal;

import static java.lang.Math.exp;
import static java.lang.Math.pow;
import static java.lang.Math.sqrt;
import static java.math.BigDecimal.ROUND_HALF_UP;
import static java.math.RoundingMode.HALF_DOWN;

public class Main {
    private static final BigDecimal SQRT_DIG = new BigDecimal(250);
    private static final BigDecimal SQRT_PRE = new BigDecimal(10).pow(SQRT_DIG.intValue());

    /**
     * Private utility method used to compute the square root of a BigDecimal.
     *
     * @author Luciano Culacciatti
     * @url http://www.codeproject.com/Tips/257031/Implementing-SqrtRoot-in-BigDecimal
     */
    private static BigDecimal sqrtNewtonRaphson  (BigDecimal c, BigDecimal xn, BigDecimal precision){
        BigDecimal fx = xn.pow(2).add(c.negate());
        BigDecimal fpx = xn.multiply(new BigDecimal(2));
        BigDecimal xn1 = fx.divide(fpx,2*SQRT_DIG.intValue(),HALF_DOWN);
        xn1 = xn.add(xn1.negate());
        BigDecimal currentSquare = xn1.pow(2);
        BigDecimal currentPrecision = currentSquare.subtract(c);
        currentPrecision = currentPrecision.abs();
        if (currentPrecision.compareTo(precision) <= -1){
            return xn1;
        }
        return sqrtNewtonRaphson(c, xn1, precision);
    }

    /**
     * Uses Newton Raphson to compute the square root of a BigDecimal.
     *
     * @author Luciano Culacciatti
     * @url http://www.codeproject.com/Tips/257031/Implementing-SqrtRoot-in-BigDecimal
     */
    public static BigDecimal bigSqrt(BigDecimal c){
        return sqrtNewtonRaphson(c,new BigDecimal("1"),new BigDecimal("1").divide(SQRT_PRE));
    }

    public static void main(String[] args) throws Exception {
        // double e=2.71828;
        BigDecimal reale=new BigDecimal("2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174135966290435729003342952605956307381323286279434907632338298807531952510190115738341879307021540891499348841675092447614606680822648001684774118537423454424371075390777449920695517027618386062613313845830007520449338265602976067371132007093287091274437470472306969772093101416928368190255151086574637721112523897844250569536967707854499699679468644549059879316368892300987931277361782154249992295763514822082698951936680331825288693984964651058209392398294887933203625094431173012381970684161403970198376793206832823764648042953118023287825098194558153017567173613320698112509961818815930416903515988885193458072738667385894228792284998920868058257492796104841984443634632449684875602336248270419786232090021609902353043699418491463140934317381436405462531520961836908887070167683964243781405927145635490613031072085103837505101157477041718986106873969655212671546889570350354");
        System.out.print("reale"+ reale.setScale(1000,ROUND_HALF_UP).toString()+"\n");

        BigDecimal e=reale; //new BigDecimal("2.71828"); // e
        BigDecimal six=new BigDecimal("624.5");
        BigDecimal e2=e.multiply(six); // e*624.5
        BigDecimal p = new BigDecimal("10");
        p=p.pow(12);               // 10^12
        e2=e2.divide(p,ROUND_HALF_UP); // e*624.5/pow(10,12)

        BigDecimal secondPart= new BigDecimal("0.3");
        secondPart=secondPart.pow(2);   // 0.3^2
        System.out.print(secondPart.setScale(1000,ROUND_HALF_UP).toString());
        System.out.print("\n");
        BigDecimal drob= new BigDecimal("2.0");
        BigDecimal den = new BigDecimal("5.0");
        drob=drob.divide(den,ROUND_HALF_UP); // 2/5
        secondPart=secondPart.add(drob); // 0.3^2+2/5
        System.out.print(secondPart.setScale(1000,ROUND_HALF_UP).toString());
        System.out.print("\n");
        BigDecimal root = bigSqrt(secondPart); // sqrt(0.3*0.3+2.0/5.0)
        System.out.print(root.setScale(1000,ROUND_HALF_UP).toString());
        System.out.print("\n");
        BigDecimal oneten= new BigDecimal("0.1");
        oneten=oneten.multiply(e);  // e*0.1
        root=root.add(oneten);
        root=root.divide(six,ROUND_HALF_UP);


        e2=e2.add(root);

       // BigDecimal gamma=new BigDecimal(e*624.5/pow(10,12)+(sqrt(0.3*0.3+2.0/5.0)+e*0.1)/624.5);

        String savedG=e2.setScale(1000,ROUND_HALF_UP).toString();

        System.out.print(savedG);
        System.out.print("Second Try"+ exp(1)+"\n");



        BigDecimal e3=reale; //new BigDecimal("2.71828");
        BigDecimal root2=new BigDecimal("0.7");
        BigDecimal p2 = new BigDecimal("10");
        p2=p2.pow(12);               // 10^12
        BigDecimal six2=new BigDecimal("624.5");
        BigDecimal oneten2= new BigDecimal("0.1");
        oneten2=oneten2.multiply(e3);  // e*0.1

        root2=root2.add(oneten2);
        root2=root2.divide(six2,ROUND_HALF_UP);

        e3=e3.multiply(six2);
        e3=e3.divide(p2,ROUND_HALF_UP);

        e3=e3.add(root2);

        String savedG2=e3.setScale(1000,ROUND_HALF_UP).toString();

        System.out.print(savedG2);
        System.out.print("End Second Try\n");








    }
}