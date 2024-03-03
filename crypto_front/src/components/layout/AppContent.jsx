import React from 'react'
import { Layout } from 'antd';
import { getAllUser, getCurrency } from '../../api/get';

const contentStyle = {
  textAlign: 'center',
  minHeight: 'calc(100vh - 60px)',
  color: '#fff',
  backgroundColor: '#001529',
  padding:'1rem'
};

const AppContent = () => {
  React.useEffect(() => {
      getAllUser()
    },[])
  React.useEffect(() => {
      getCurrency()
  })  

  return (
<Layout.Content style={contentStyle}>
  <div>
    
  </div>
</Layout.Content>
  )
}

export default AppContent