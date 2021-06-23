import { Component, OnInit, Input,} from '@angular/core';




@Component({
  selector: 'app-order-card',
  templateUrl: './order-card.component.html',
  styleUrls: ['./order-card.component.css']
})
export class OrderCardComponent implements OnInit {

  // possible map for the card colors, 
  //The present will depend on the status of the order.
  statusInfo = {
    beforPayment: {
      bgColor: 'bg-secondary',
      faIcon: 'fa-comment-dollar',
      info1: '',
      info2:'',
    },
    preparation: {
      bgColor: 'bg-info',
      faIcon: 'fa-spinner fa-spin',
      info1: '',
      info2:'',
    },
    ready: {
      bgColor: 'bg-danger',
      faIcon: 'fa-exclamation-circle',
      info1: '',
      info2:'',
    },
    delivering: {
      bgColor: 'bg-warning',
      faIcon: 'fa-shoe-prints',
      info1: '',
      info2:'',
    },
    finish: {
      bgColor: 'bg-success',
      faIcon: 'fa-check-circle',
      info1: '',
      info2:'',
    },
  };

  // orderData: any = {
  //   name: 'matan',
  //   status: 'delivering',
  //   items: [
  //     {
  //       name: 'ציפס 🍟',
  //       price: 12.9,
  //     },
  //     {
  //       name: 'קולה 🥤',
  //       price: 8.5,

  //     },
  //     {
  //       name: 'גחנון 🍞',
  //       price: 24,
  //     },
  //   ]
  // }
  @Input() orderData: any;
  constructor() { }

  ngOnInit(): void {
  }

}
