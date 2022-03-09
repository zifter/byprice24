import React from 'react';
import PropTypes from 'prop-types';
import {
  Div, Text, Container,
} from 'atomize';

const TextContact = ({text, bottomValue, textSize, textWeight,
  tag, children}) => {
  return (
    <Div itemScope itemType="http://schema.org/Organization" textAlign="left">
      <Text itemProp="email" tag={tag || 'section'}
        textSize={textSize || 'paragraph'}
        textWeight={textWeight || '400'}
        m={{b: bottomValue}}>
        {text}
        <a href="mailto:contact@findprice.by">
          <span>{children}</span></a>
      </Text>
    </Div>
  );
};
TextContact.propTypes = {
  text: PropTypes.string.isRequired,
  bottomValue: PropTypes.string,
  textSize: PropTypes.string,
  textWeight: PropTypes.string,
  tag: PropTypes.string,
  children: PropTypes.string,
};
const Contacts = () => {
  return (
    <Container p="0" m={{t: '2rem', l: '12rem'}} d="flex"
      flexDir="column" align="flex-start">
      <TextContact tag={'h1'} text={'Контакты'} textSize={'display1'}
        bottomValue={'0.5rem'} textWeight={'600'}/>
      <TextContact text={'У Вас возникли вопросы? Мы здесь чтобы помочь.'}
        bottomValue={'1.7rem'}/>
      <TextContact text='e-mail: '>contact@findprice.by
      </TextContact>
    </Container>
  );
};

export default Contacts;
