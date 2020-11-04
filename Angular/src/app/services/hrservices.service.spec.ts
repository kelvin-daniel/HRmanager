import { TestBed } from '@angular/core/testing';

import { HrservicesService } from './hrservices.service';

describe('HrservicesService', () => {
  let service: HrservicesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HrservicesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
