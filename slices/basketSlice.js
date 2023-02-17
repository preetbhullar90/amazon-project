import { createSlice } from '@reduxjs/toolkit';


const initialState = {
     items: [], 
    };

export const basketSlice = createSlice({
  name: 'basket',
  initialState,
  reducers: {
    addToBasket(state,action) {
        state.items=[...state.items,action.payload]
    },
    removeToBasket(state, action) {},

  },
})

export const { addToBasket, removeToBasket} = basketSlice.actions


export const selectItems = (state)=> state.basket.items;

export default basketSlice.reducer
