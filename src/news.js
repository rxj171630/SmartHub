import {Card} from 'semantic-ui-react'
import React from 'react'

class NewsComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: []
    };
  }


  processResult(result) {
      if (!result) {
          console.log(result);
          return;
      } else {
          var res = []
          result.articles.forEach(function (item, index) {
            res.push({header: item.title, description: item.description, meta: item.publishedAt})
          });
          return res.slice(0, 4);
      }
  }

  componentDidMount() {
    fetch("http://192.168.86.41:8000/news")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            items: this.processResult(result)
          });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error: error
          });
        }
      )
  }

  render() {
    const { error, isLoaded, items } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
          <Card.Group items={items} />
      );
    }
  }
}

export default NewsComponent
