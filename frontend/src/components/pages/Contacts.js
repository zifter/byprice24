import React from 'react';
import PropTypes from 'prop-types';
import {
  Div, Text, Container,
} from 'atomize';

const TextContact = ({text, bottomValue, textSize}) => {
  return (
    <Div textAlign="left">
      <Text tag="section" textSize={textSize || 'paragraph'} textWeight="400"
        m={{b: bottomValue}}>
        {text}
      </Text>
    </Div>
  );
};
TextContact.propTypes = {
  text: PropTypes.string.isRequired,
  bottomValue: PropTypes.string,
  textSize: PropTypes.string,
};
const Contacts = () => {
  return (<>
    <Container p="0" d="flex" flexDir="column" align="flex-start">

      <Div
        textAlign="left">
        <Text tag="h1" textSize="display1" textWeight="600" m={{b: '0.5rem'}}>
          Контакты
        </Text>
      </Div>
      <TextContact text={'У Вас возникли вопросы? Мы здесь чтобы помочь.'}
        bottomValue={'1.7rem'}/>
      <TextContact text={'Информация о компании:'} textSize={'heading'} />
      <TextContact text={'UAB Elektroninės prekybos centras'}
        bottomValue={'0'}/>
      <TextContact text={'Код предприятия: 304298127'}/>
      <TextContact text={'НДС код: LT100010323218'}
        bottomValue={'1.7rem'}/>
      <TextContact text={'Адрес:'} textSize={'heading'}/>
      <TextContact text={'Laisvės pr. 60-1107, LT-05120 Vilnius'}
        bottomValue={'1.7rem'}/>
      <TextContact text={'E. почта: contact@findprice.by'}/>
    </Container>
  </>
  );
};

export default Contacts;
