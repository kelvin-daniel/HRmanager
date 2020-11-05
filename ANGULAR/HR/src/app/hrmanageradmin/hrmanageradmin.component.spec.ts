import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HrmanageradminComponent } from './hrmanageradmin.component';

describe('HrmanageradminComponent', () => {
  let component: HrmanageradminComponent;
  let fixture: ComponentFixture<HrmanageradminComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HrmanageradminComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HrmanageradminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
