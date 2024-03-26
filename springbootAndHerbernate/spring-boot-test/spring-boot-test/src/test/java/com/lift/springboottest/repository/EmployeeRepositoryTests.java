package com.lift.springboottest.repository;

import com.lift.springboottest.model.Employee;
import static org.assertj.core.api.Assertions.assertThat;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;

import java.util.List;


@DataJpaTest
public class EmployeeRepositoryTests {

    private final EmployeeRepository employeeRepository;

    @Autowired
    public EmployeeRepositoryTests(EmployeeRepository employeeRepository) {
        this.employeeRepository = employeeRepository;
    }

    //junit test for save employee
    @DisplayName("Junit Save Employee")
    @Test
    public void givenEmployeeObject_whenSave_thenReturnSavedEmployee(){

        //given - precondition or setup
        Employee employee = Employee.builder()
                .firstName("Lift")
                .lastName("Za")
                .email("Lift@Za.com")
                .build();
        //when - action or the behaviour
        Employee savedEmployee = employeeRepository.save(employee);

        //then - verify the output
        assertThat(savedEmployee).isNotNull();
        assertThat(savedEmployee.getId()).isGreaterThan(0);
    }

    //JUnit test for findAll
    @DisplayName("Junit findAll Employee")
    @Test
    public void givenEmployeesList_whenFindAll_thenEmployeesList(){
        //given - precondition or setup
        Employee employee = Employee.builder()
                .firstName("Lift")
                .lastName("Za")
                .email("Lift@Za.com")
                .build();

        Employee employee1 = Employee.builder()
                .firstName("Love")
                .lastName("Za")
                .email("Love@Za.com")
                .build();

        Employee employee2 = Employee.builder()
                .firstName("Loof")
                .lastName("Za")
                .email("Loof@Za.com")
                .build();

        employeeRepository.save(employee);
        employeeRepository.save(employee1);
        employeeRepository.save(employee2);
        //when - action or the behaviour
        List<Employee> employeeList = employeeRepository.findAll();

        //then - verify the output

        assertThat(employeeList).isNotNull();
        assertThat(employeeList.size()).isEqualTo(3);
    }


    //junit test for get employee by id
    @DisplayName("Junit findById Employee")
    @Test
    public void givenEmployeeObject_whenFindById_thenReturnEmployeeObject(){
        //given - precondition or setup
        Employee employee0 = Employee.builder()
                .firstName("Lift")
                .lastName("Za")
                .email("Lift@Za.com")
                .build();

        Employee employee1 = Employee.builder()
                .firstName("Love")
                .lastName("Za")
                .email("Love@Za.com")
                .build();

        Employee employee2 = Employee.builder()
                .firstName("Loof")
                .lastName("Za")
                .email("Loof@Za.com")
                .build();

        employeeRepository.save(employee0);
        employeeRepository.save(employee1);
        employeeRepository.save(employee2);
        //when - action or the behaviour
        Employee employee = employeeRepository.findById(employee0.getId()).get();
        //then - verify the output

        assertThat(employee).isNotNull();
    }

    //junit test for findByEmail
    @DisplayName("Junit findByEmail Employee")
    @Test
    public void givenEmployeeEmail_whenFindByEmail_thenmployeeEmail(){

        //given - precondition or setup
        Employee employee0 = Employee.builder()
                .firstName("Lift")
                .lastName("Za")
                .email("Lift@Za.com")
                .build();
        employeeRepository.save(employee0);
        //when - action or the behaviour
        Employee employee = employeeRepository.findByEmail(employee0.getEmail()).get();
        //then - verify the output
        assertThat(employee).isNotNull();
    }

    //junit test for findByEmail
    @DisplayName("Junit findByFirstName Employee")
    @Test
    public void givenEmployeeFirstName_whenFindByFirstName_thenmployeeFistName(){

        //given - precondition or setup
        Employee employee0 = Employee.builder()
                .firstName("Lift")
                .lastName("Za")
                .email("Lift@Za.com")
                .build();
        employeeRepository.save(employee0);
        //when - action or the behaviour
        Employee employee = employeeRepository.findByFirstName(employee0.getFirstName()).get();
        //then - verify the output
        assertThat(employee).isNotNull();
        assertThat(employee).isEqualTo(employee0);
    }

    //junit test for findByEmail
    @DisplayName("Junit Update Employee")
    @Test
    public void givenEmployeeObject_whenUpdateEmployee_thenUpdatedEmployee(){

        //given - precondition or setup
        Employee employee0 = Employee.builder()
                .firstName("Lift")
                .lastName("Za")
                .email("Lift@Za.com")
                .build();
        employeeRepository.save(employee0);
        //when - action or the behaviour
        Employee employee = employeeRepository.findById(employee0.getId()).get();
        employee.setEmail("Updated@Za.com");
        employee.setFirstName("Love");
        Employee updatedEmployee = employeeRepository.save(employee);
        //then - verify the output
        assertThat(updatedEmployee).isNotNull();
        assertThat(updatedEmployee.getEmail()).isEqualTo("Updated@Za.com");
        assertThat(updatedEmployee.getFirstName()).isEqualTo("Love");
    }



}
