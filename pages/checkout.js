import Header from '../components/Header';
import { store } from '../apps/store';
import { Provider} from 'react-redux';
import CheckoutProduct from '../components/CheckoutProduct';


const Checkout = () => {

  


  return (
    <div>

 
    <Provider  store={store}>
    <Header />

    
   
     <CheckoutProduct />
     </Provider>
 


    </div>
  )
}

export default Checkout