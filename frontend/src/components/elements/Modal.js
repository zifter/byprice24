import React from 'react';
import {Link} from 'react-router-dom';
import {
  Div,
  Text,
} from 'atomize';
import PropTypes from 'prop-types';
import './Modal.css';


const Modal = ({searchInModalWindow, setSearchInModalWindow}) => {
  let width = '';
  if (document.getElementById('input-search')) {
    width = document.getElementById('input-search')
        .clientWidth + 'px';
  }
  return (<>
    {searchInModalWindow && searchInModalWindow.map((t, i)=>{
      return (<Div
        key={t.id}
        cursor="pointer"
        w={width}
        className="modal"
        pos="relative"
        p={{x: '1rem', y: '0.75rem'}}
        rounded={i === 0 ? {tl: 'md', tr: 'md'} :
          (i === searchInModalWindow.length - 1) ?
          {bl: 'md', br: 'md'}:''}
        bg="gray100"
        shadow="5"
        hoverBg="gray400"
      >
        <Link to={`/products/${t.id}`}>
          <Text textColor="black"
            onClick={()=>{
              setSearchInModalWindow([]);
            }}>{t.name}</Text>
        </Link>
      </Div>);
    })
    }
  </>
  );
};

Modal.propTypes = {
  searchInModalWindow: PropTypes.array,
  setSearchInModalWindow: PropTypes.function,
};
export default Modal;
