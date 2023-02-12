import Image from "next/image";
import { useState, useEffect} from "react";
import { StarIcon } from '@heroicons/react/24/outline';
import CurrencyFormat from 'react-currency-format';

  

const MAX_RATING = 5;
const MIN_RATING = 1;


const Product = ({id, title, price, description, category, image}) => {
  
    const [rating, SetRating] = useState(
        Math.floor(Math.random()* (MAX_RATING - MIN_RATING + 1)) + MIN_RATING
    );

    const [hasPrime, SetHasPrime] = useState(Math.random() < 0.5)


    useEffect(() => {
        SetRating(rating);
    }, []);

    useEffect(() => {
        SetHasPrime(hasPrime);
    }, []);
  
  
    return (
        
    <div className="relative flex flex-col m-5 bg-white z-30 p-10">
    
           
    <p className="absolute top-2 right-2 text-xs italic text-gray-400">{category}</p>
    <Image 
     src={image} height={200} width={200} props='contain'  
    />

    <h4 className="my3">{title}</h4>
    <div className="flex">


{Array(SetRating).fill().map((_, i)=>(

<StarIcon  className="h-5 text-yellow-400" />
))}
    </div>

    <p className="text-sm my-2 line-clamp-2">{description}</p>
    <div className="mb-5">
<CurrencyFormat value={price} displayType={'text'} thousandSeparator={true} prefix={'£'} renderText={value => <div>{value}</div>}/>
   
    </div>

    {SetHasPrime && (
        <div className="flex items-center space-x-2 -mt-5">
            <img className="w-12" src="https://links.papareact.com/fdw" alt="" />
            <p className="text-xs text-gray-500">Free Next-day Delivery</p>
        </div>
    )}
    <button className="mt-auto button">Add to Basket</button>

    </div>
  )
}

export default Product;