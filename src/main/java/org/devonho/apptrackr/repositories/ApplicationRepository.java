package org.devonho.apptrackr.repositories;

import java.util.List;
import org.devonho.apptrackr.models.Application;

import org.springframework.data.mongodb.repository.MongoRepository;

public interface ApplicationRepository extends MongoRepository<Application, String> {
       

}
