import CheckoutAll from '../components/CheckoutAll';
import { useSelector } from 'react-redux';
import { selectItems } from '../slices/basketSlice';
import Image from 'next/image';

const CheckoutProduct = () => {


const items = useSelector(selectItems)
 
  return (
    <div className='flex-grow m-5 shadow-sm'>
    <Image 
        src="https://links.papareact.com/ikj"
        width={1020}
        height={250}
        style={{objectFit:'contain'}}
    />
    <div className='flex flex-col p-5 space-y-10 bg-white'>
    <h1 className='text-3xl border-b pb-4'>
      {items.length ===0 ? "Your Amazon Basket is empty." : "Shopping Basket"}
    </h1>

    </div>


  {items.map(({ id,title,price,description,category,image,rating,hasPrime, i})=>(
      <CheckoutAll  
        key = {i}
        id={id}
        title = {title} 
        price = {price} 
        description = {description} 
        category = {category} 
        image = {image}
        hasPrime= {hasPrime}
        rating = {rating}
      />
    ))}

   
    </div>
  )
}

export default CheckoutProduct