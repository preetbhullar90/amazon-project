import Image from "next/image";
import { useState } from "react";
import { StarIcon } from '@heroicons/react/24/outline';


const MAX_RATING = 5;
const MIN_RATING = 1;

const CheckoutAll = ({id, title,  hasPrime, price, description, category, image}) => {

    const [rating, SetRating] = useState(
        Math.floor(Math.random()* (MAX_RATING - MIN_RATING + 1)) + MIN_RATING
        
    );

  return (
    <div>
    
    <div>
    <p className="text-gray-400">{category}</p>
    <Image className="flex items-center"
        src={image}
        width={200}
        height={200}
    />

    <p className="text-2xl py-3">{title}</p>
    <div className="flex">

    {Array(rating).fill().map((_, i)=>(

<StarIcon  className=" h-5 text-yellow-400" />
))}
    </div>
    <p className="line-clamp-2">{description}</p>
    <p className="py-3">{price}</p>

    {hasPrime && (

        <img className="w-12" src="https://links.papareact.com/fdw" alt="" />
    )}
    </div>
    
    
    </div>
  )
}

export default CheckoutAll;